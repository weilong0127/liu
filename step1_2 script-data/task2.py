
#delete the cluster name line of cdhit file
line=open('fas.clstr','r').readlines()

clusternohead=open('clusternohead.txt','w')
for i in line:
    if i[0] != '>':
        clusternohead.write(i)
clusternohead.close()


# delete the useless part of cdhit file
clline=open('clusternohead.txt','r').readlines()
clusterfinal=open('clusterfinal.txt','w')
for i in clline:
    for x in range(len(i)):
        if i[x] == '>':
            clusterfinal.write(i[0]+' '+i[x:]+'\n')
            
clusterfinal.close()

#delete 
fff=open('clusterfinal.txt','r').readlines()
clusterf=open('clusterf.txt','w')
for ii in fff:
    for xx in range(len(ii)):
        if ii[xx:xx+3] == '...':
            clusterf.write(ii[:xx])
            clusterf.write('\n')
clusterf.close()            



#devide final cdhit file into a list, where the line is one set and every item in one line is the name of seq.



cf=open('clusterf.txt','r').read().splitlines()
output=open('output.txt','w')
a=0
b=60
o1=''
for x in cf:
    if b<len(cf):
        if (b-a)>= 60 and cf[b][0]== '0': 
            o1=cf[a:b]
            for itt in o1:
                itt=itt[2:]
                output.write(itt)
                output.write(' ')
            output.write('\n')
            a=b
            b=b+60
            continue
        else:
            b=b+1

    else:
        o1=cf[a:b]
        for itt in o1:
            itt=itt[2:]
            output.write(itt)
            output.write(' ')
        break

output.close()



#seperate output into 6 files(5train+1test)
trnum=1
while trnum<=5:
    tttt=open('train'+str(trnum)+'.txt','w')
    tttt.write(open('output.txt','r').readlines()[trnum-1].replace(' ','\n')[:-2])
    trnum=trnum+1
    tttt.close()
if trnum==6:
    test=open('train'+str(trnum)+'.txt','w')
    test.write(open('output.txt','r').readlines()[5].replace(' ','\n')[:-1])
    test.write(open('output.txt','r').readlines()[6].replace(' ','\n')[:-2])
    test.close()



#y is the line number of a sequence in namelist
def length(x):
    seqlist=open('seqlist.txt','r')
    a=0
    while x==0:
        return 0
    for linea in seqlist.read().split('\n')[0:x]:
        a=a+len(linea)
    return a

def id(y):
    fid=open('featureid.txt','r').read().split('\n')
    return fid[length(y-1):length(y)]

#create a dictionary seqname:a string of features
seqname=open('namelist.txt','r').read().replace('>','').split('\n')
c=0
dict={}
for i in range(len(seqname)):
    for o in id(c+1):
        dict.setdefault(seqname[c],[]).append(o)
    c=c+1
    

#translate file by dictionary
set_number=1
while set_number<=6:
    train2=open('train'+str(set_number)+'.txt','r').read().replace('>','').split('\n')
    set2=open('set'+str(set_number)+'.txt','w')
    sss2=''
    for g in train2:
        sss2=dict[g]
        for s in sss2:
            set2.write(s)
            set2.write('\n')
    set2.close()
    set_number=set_number+1




