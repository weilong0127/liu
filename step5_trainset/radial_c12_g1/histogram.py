'''
import math
mcc=open('mcc.txt','w')
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
mcc.close()
'''
import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

means = open('mcc.txt','r').read().splitlines()
fig, ax = plt.subplots()
#n_groups = 2
index = np.arange(1,3,1)
bar_width = 0.35
error_config = {'ecolor': '0.3'}
rect = plt.bar(index, means, bar_width, alpha=0.4, color='b', error_kw=error_config)
autolabel(rect)
plt.axis([0, 3, 0, 0.4])
plt.xlabel('kernels')
plt.ylabel('MCC value')
plt.title('MCC comparison of four basic kernels')
plt.xticks(index + bar_width/2, ('c1', 'c2'))
plt.tight_layout()
plt.show()
