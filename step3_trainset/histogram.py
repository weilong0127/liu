
import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')


means = open('mcc1-5.txt','r').read().splitlines()
means+=open('mcc.txt','r').read().splitlines()
means+=open('C:/Users/admin/Desktop/project/step3_trainset/set_6/mcc.txt','r').read().splitlines()
fig, ax = plt.subplots()

index = np.arange(1,8,1)
bar_width = 0.35

error_config = {'ecolor': '0.3'}

rect = plt.bar(index, means, bar_width,
                 alpha=0.4,
                 color='b',

                 error_kw=error_config)

autolabel(rect)
plt.axis([0, 8, 0, 0.16])
plt.xlabel('Group')
plt.ylabel('MCC')
plt.title('Matthews correlation coefficient ')
plt.xticks(index + bar_width/2, ('set1', 'set2', 'set3', 'set4', 'set5', 'set1-5','set6'))
plt.tight_layout()
plt.show()
