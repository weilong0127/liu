
#blast files
namelist=open('namelist.txt','r').read().split('\n')
seqlist=open('seqlist.txt','r').read().split('\n')
i=0
for x in namelist:
	f=open('sequence'+str(i)+'.fasta','w')
	f.write('>'+namelist[i]+'\n'+seqlist[i])
	i=i+1
	f.close()