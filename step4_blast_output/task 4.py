'''
#judge in position of (linenumber,rownumber) is Helix or not
def position_h(linen,rown):
        strlist=open('strlist.txt','r').read().split('\n')
        if strlist[linen][rown] == 'H':
                return '+1'
        else:
                return '-1'
        strlist.close()

#the line number (below) is the row number above. the name of file (below) is the line number above.                
import math
n=0
strlist=open('strlist.txt','r').read().splitlines()
while (n<=398):
        seq='sequence'+str(n)
        lines=open(seq+'.psi','r').readlines()[3:-6]
        w=open(seq+'.txt','w')
        ln=0
        for line in lines:
                rn=1
                w.write(position_h(n,ln)+' ')
                for i in line.split()[2:22]:
                        w.write('%d' %rn+':'+'%.4f' %(float(1/(1+math.exp(-float(i)))))+' ')
                        rn=rn+1
                ln=ln+1
                w.write('\n')      
        w.close()
        ln=0
        n=n+1
       
'''    
#build a dict {name:seqfileabove}
seqname=open('namelist.txt','r').read().replace('>','').split('\n')
c=0
dict={}
for i in range(len(seqname)):
        ss='sequence'+str(c)
        psi=open(ss+'.txt','r').read().splitlines()
        for o in psi:
                dict.setdefault(seqname[c],[]).append(o)
        c=c+1

#translate cdhit file by this dict
trainn=1
while (trainn<=6):
        trainname='train'+str(trainn)
        setname='set'+str(trainn)
        train1=open(trainname+'.txt','r').read().replace('>','').split('\n')
        set1=open(setname+'.svm','w')
        for g in train1:
            sss1=''
            sss1=dict[g]
            for s in sss1:
                set1.write(s)
                set1.write('\n')
        set1.close()
        trainn=trainn+1
        

