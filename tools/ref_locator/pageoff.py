import sys,re,collections
# usage: pageoff.py file  -> prints number of ff pages, most common (ffindex - printed) offsets, and sample
txt=open(sys.argv[1],encoding='utf-8',errors='replace').read()
pages=txt.split('\f')
print("ff pages:",len(pages), "chars:",len(txt))
offs=collections.Counter(); samples={}
for i,p in enumerate(pages):
    lines=[l.strip() for l in p.strip().split('\n') if l.strip()]
    cand=lines[:3]+lines[-3:]
    for l in cand:
        m=re.fullmatch(r'[—\-–\s]*(\d{1,4})[—\-–\s]*',l)
        if not m:
            m=re.match(r'^(\d{1,4})\s+\S',l) or re.search(r'\S\s+(\d{1,4})$',l)
        if m:
            n=int(m.group(1))
            if 0<n<3000:
                offs[i-n]+=1
                samples.setdefault(i-n,(i,n,l[:60]))
for o,c in offs.most_common(6):
    print(f"offset ff-printed={o}: {c} hits, e.g. ffpage {samples[o][0]} printed {samples[o][1]} line {samples[o][2]!r}")
