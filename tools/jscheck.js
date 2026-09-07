const fs=require('fs'),vm=require('vm');
const h=fs.readFileSync('site/risheh.html','utf8');
const re=/<script>([\s\S]*?)<\/script>/g; let m,n=0;
while((m=re.exec(h))){new vm.Script(m[1]);n++;}
console.log('js ok',n,'scripts');
