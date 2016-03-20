
import numpy as np
import matplotlib.pyplot as plt
def autolabel(rects): 
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

n_groups = 4
means = open('mcc.txt','r').read().splitlines()
means.append(float(open('C:/Users/admin/Desktop/project/step3_trainset/mcc.txt','r').read().splitlines()[0]))
fig, ax = plt.subplots()
index = np.arange(1,6,1)
bar_width = 0.35
error_config = {'ecolor': '0.3'}
rect = plt.bar(index, means, bar_width,
                 alpha=0.4,
                 color='b',
                 error_kw=error_config)
autolabel(rect)
plt.axis([0, 6, 0, 0.4])
plt.xlabel('kernels')
plt.ylabel('MCC value')
plt.title('MCC comparison of four basic kernels')
plt.xticks(index + bar_width/2, ('linear', 'polynomial', 'RBF', 'sigmoid','single sequence'))
plt.tight_layout()
plt.show()
