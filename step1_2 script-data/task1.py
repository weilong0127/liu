
f=open('stride.3line','r')
seq=f.readlines()
namelist=open('namelist.txt','w')
seqlist=open('seqlist.txt','w')
strlist=open('strlist.txt','w')
i=1
for x in seq:
        if (i%3==1): 
                namelist.write(x[1:])
                i=i+1
        elif (i)%3==2:
                seqlist.write(x)
                i=i+1
        elif (i%3==0):
                strlist.write(x)
                i=i+1
f.close()

namelist.close()
seqlist.close()
strlist.close()


dict = {'G':'1','A':'2','V':'3','L':'4','I':'5','F':'6','W':'7','Y':'8','D':'9','N':'10','E':'11','K':'12','Q':'13','M':'14','S':'15','T':'16','C':'17','P':'18','H':'19','R':'20'}
sel = open('seqlist.txt','r').read()
stl = open('strlist.txt','r').read()
p=0
featureid=open('featureid.txt','w')

for b in sel:
        if stl[p] == 'H':
                featureid.write('+1 '+dict[b]+':1'+'\n')
                p=p+1
        elif stl[p] == '\n':
                p=p+1
        else:
                featureid.write('-1 '+dict[b]+':1'+'\n')
                p=p+1        

featureid.close()

        


