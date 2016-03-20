
import numpy as np
import matplotlib.pyplot as plt
def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

means=open('mcc.txt','r').read().splitlines()[:2]
means+=open('C:/Users/admin/Desktop/project/step5_trainset/radial_c12_g1/mcc.txt','r').read().splitlines()
means.append(open('mcc.txt','r').read().splitlines()[2])
means.append(open('C:/Users/admin/Desktop/project/step5_trainset/mcc.txt','r').read().splitlines()[2])
means+=open('C:/Users/admin/Desktop/project/step3_trainset/mcc.txt','r').read().splitlines()

fig, ax = plt.subplots()
index = np.arange(1,8,1)
bar_width = 0.35
error_config = {'ecolor': '0.3'}
rect = plt.bar(index, means, bar_width,
                 alpha=0.4,
                 color='b',
                 error_kw=error_config)
autolabel(rect)
plt.axis([0, 8, 0, 0.4])
plt.xlabel('kernels')
plt.ylabel('MCC value')
plt.title('MCC comparison of RBF parameters')
plt.xticks(index + bar_width/2, ('c2g0.5', 'c8g0.5', 'c1g1', 'c2g1', 'c2g2', 'RBF', 'single sequence'))
plt.tight_layout()
plt.show()

