j=0
while j<=3:
    i=1
    w=open('roc'+str(j)+'.txt','w+')
    while i<=5:
        setname=open('set'+str(i)+'.svm','r').read().splitlines()
        predname=open('set'+str(i)+'.svm'+str(j)+'.pred','r').read().splitlines()
        for n in range(len(setname)):
                
                w.write(setname[n][:2]+' '+predname[n]+'\n')
        i=i+1
    w.close()
    lines=open('roc'+str(j)+'.txt','r').read().splitlines()
    ww=open('sortedroc'+str(j)+'.txt','w+')
    for li in sorted(lines, key=lambda line:float(line.split()[1])):
        ww.write(li+'\n')
    ww.close()
    i=0
    j=j+1

