
import math
mcc=open('mcc.txt','w')
ac=open('accuracy.txt','w')
j=1
while j<=2:
    i=1
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    while i<=5:

        setname=open('set'+str(i)+'.svm','r').read().splitlines()
        predname=open('set'+str(i)+'.svm'+str(j)+'1.pred','r').read().splitlines()
        for n in range(len(setname)):

            if setname[n][:2] == '+1' and float(predname[n])>0:
                tp=tp+1
            if setname[n][:2] == '+1' and float(predname[n])<0:
                fp=fp+1
            if setname[n][:2] == '-1' and float(predname[n])<0:
                tn=tn+1
            if setname[n][:2] == '-1' and float(predname[n])>0:
                fn=fn+1
        i=i+1
    mcc.write('%0.6f'%(((tp*tn - fp*fn) / math.sqrt( (tp + fp)*(tp + fn)*(tn + fp)*(tn + fn) )))+'\n')
    j=j+1
    ac.write(format(float((tp+tn))/float((tp+tn+fp+fn)),'2%')+'\n')
ac.close()
mcc.close()
