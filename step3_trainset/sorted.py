
i=1
w=open('roc.txt','w+')
while i<=5:
    setna='set'
    setna+=str(i)
    setname=open(setna+'.svm','r').read().splitlines()
    predname=open(setna+'.svm.pred','r').read().splitlines()
    for n in range(len(setname)):
            
            w.write(setname[n][:2]+' '+predname[n]+'\n')
    i=i+1
w.close()

lines=open('roc.txt','r').read().splitlines()
ww=open('sortedroc.txt','w+')
for li in sorted(lines, key=lambda line:float(line.split()[1])):
    ww.write(li+'\n')
ww.close()
