import re,sys
def clean(fn):
    out=[];prev=''
    for l in open(fn,encoding='utf8'):
        l=l.strip()
        if not l or l.startswith(('WEBVTT','Kind:','Language:','NOTE')) or '-->' in l: continue
        l=re.sub(r'<[^>]+>','',l).strip()
        if not l or l==prev: continue
        out.append(l);prev=l
    # drop lines that are prefix of next line (rolling)
    res=[]
    for i,l in enumerate(out):
        if i+1<len(out) and out[i+1].startswith(l): continue
        res.append(l)
    return ' '.join(res)
for id in sys.argv[1:]:
    t=clean(f'{id}.en-orig.vtt')
    open(f'{id}.txt','w').write(t)
    print(id,len(t.split()))
