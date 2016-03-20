
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
dict={0:'r',1:'y',2:'g',3:'b'}
dict2={0:'linear: ', 1:'polynomial: ', 2:'RBF: ', 3:'sigmoid: '}
i=0
while i<=3:
    actual = []
    predictions = []
    sortroc=open('sortedroc'+str(i)+'.txt','r').readlines()
    for line in sortroc:
        actual.append(float(line.split()[0]))
        predictions.append(float(line.split()[1]))
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, dict[i], label=dict2[i]+'%0.4f'% roc_auc)
    plt.plot([0,1],[0,1],'r--')    
    i=i+1
actual = []
predictions = []
sortroc=open('C:/Users/admin/Desktop/project/step3_trainset/sortedroc.txt','r').readlines()
for line in sortroc:
    actual.append(float(line.split()[0]))
    predictions.append(float(line.split()[1]))
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.plot(false_positive_rate, true_positive_rate, 'purple', label='single sequence: '+'%0.4f'% roc_auc)
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.legend(loc='lower right')
plt.title('Receiver Operating Characteristic')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

