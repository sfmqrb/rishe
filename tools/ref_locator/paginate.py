#!/usr/bin/env python3
"""usage: paginate.py <identifier> <out.txt> [basename-filter]
Builds a local text with \f between leaves (leaf i == ff-page i, 0-based) from IA hocr_searchtext+pageindex,
falling back to djvu.xml. Prints page_numbers-derived offset."""
import sys,json,gzip,io,re,collections,urllib.request,urllib.parse,html
ident,out=sys.argv[1],sys.argv[2]; filt=sys.argv[3] if len(sys.argv)>3 else ''
meta=json.load(urllib.request.urlopen(f'https://archive.org/metadata/{ident}'))
names=[f['name'] for f in meta['files'] if filt in f['name']]
def get(name):
    u=f'https://archive.org/download/{ident}/'+urllib.parse.quote(name)
    r=urllib.request.urlopen(u,timeout=300); data=r.read()
    if name.endswith('.gz'): data=gzip.decompress(data)
    return data
pi=[n for n in names if n.endswith('_hocr_pageindex.json.gz')]
st=[n for n in names if n.endswith('_hocr_searchtext.txt.gz')]
pages=[]
if pi and st:
    idx=json.loads(get(pi[0])); txt=get(st[0])
    for e in idx:
        pages.append(txt[e[0]:e[1]].decode('utf-8','replace'))
    src='hocr'
else:
    xmls=[n for n in names if n.endswith('_djvu.xml')]
    if not xmls: print('NO SOURCE',names); sys.exit(1)
    data=get(xmls[0]).decode('utf-8','replace')
    for obj in re.split(r'<OBJECT\b',data)[1:]:
        lines=[]
        for ln in re.findall(r'<LINE>(.*?)</LINE>',obj,re.S):
            words=re.findall(r'<WORD[^>]*>(.*?)</WORD>',ln,re.S)
            lines.append(html.unescape(' '.join(words)))
        pages.append('\n'.join(lines))
    src='djvuxml'
open(out,'w',encoding='utf-8').write('\f'.join(pages))
print(f'{ident}: {len(pages)} leaves written to {out} via {src}, {sum(len(p) for p in pages)} chars')
pn=[n for n in names if n.endswith('_page_numbers.json')]
if pn:
    d=json.loads(get(pn[0]))
    offs=collections.Counter(); ex={}
    for p in d['pages']:
        s=p.get('pageNumber') or ''
        if s.isdigit():
            o=p['leafNum']-int(s); offs[o]+=1; ex.setdefault(o,(p['leafNum'],int(s)))
    for o,c in offs.most_common(4):
        print(f'  page_numbers: leaf = printed + {o}  ({c} leaves, e.g. leaf {ex[o][0]} = p.{ex[o][1]})')
    nums=[int(p['pageNumber']) for p in d['pages'] if (p.get('pageNumber') or '').isdigit()]
    if nums: print(f'  printed range {min(nums)}-{max(nums)}')
