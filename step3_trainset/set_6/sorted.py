
i=1
w=open('roc.txt','w+')

setname=open('set6.svm','r').read().splitlines()
predname=open('set6.svm.pred','r').read().splitlines()
for n in range(len(setname)):           
    w.write(setname[n][:2]+' '+predname[n]+'\n')

w.close()

lines=open('roc.txt','r').read().splitlines()
ww=open('sortedroc.txt','w+')
for li in sorted(lines, key=lambda line:float(line.split()[1])):
    ww.write(li+'\n')
ww.close()
