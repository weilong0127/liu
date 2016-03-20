
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
dict={20.5:'r',22:'y',80.5:'g',11:'b',21:'grey'}
dict2={20.5:'c2g0.5: ', 22:'c2g2: ', 80.5:'c8g0.5: ', 11:'c1g1: ',21:'c2g1'}
for j in ('20.5','80.5','22'):
    actual = []
    predictions = []
    sortroc=open('sortedroc'+j+'.txt','r').readlines()
    for line in sortroc:
        actual.append(float(line.split()[0]))
        predictions.append(float(line.split()[1]))
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, dict[float(j)], label=dict2[float(j)]+'%0.4f'% roc_auc)  
for i in ('11','21'):
    actual = []
    predictions = []
    sortroc=open('C:/Users/admin/Desktop/project/step5_trainset/radial_c12_g1/sortedroc'+i+'.txt','r').readlines()
    for line in sortroc:
        actual.append(float(line.split()[0]))
        predictions.append(float(line.split()[1]))
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, dict[float(i)], label=dict2[float(i)]+'%0.4f'% roc_auc)
actual = []
predictions = []
sortroc=open('C:/Users/admin/Desktop/project/step5_trainset/sortedroc2.txt','r').readlines()
for line in sortroc:
    actual.append(float(line.split()[0]))
    predictions.append(float(line.split()[1]))
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.plot(false_positive_rate, true_positive_rate, 'purple', label='default RBF: '+'%0.4f'% roc_auc)
actual = []
predictions = []
sortroc=open('C:/Users/admin/Desktop/project/step3_trainset/sortedroc.txt','r').readlines()
for line in sortroc:
    actual.append(float(line.split()[0]))
    predictions.append(float(line.split()[1]))
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.plot(false_positive_rate, true_positive_rate, 'black', label='single sequence: '+'%0.4f'% roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.legend(loc='lower right')
plt.title('Receiver Operating Characteristic')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

