
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random

actual = []
predictions = []
sortroc=open('sortedroc.txt','r').readlines()
for line in sortroc:
    actual.append(float(line.split()[0]))
    predictions.append(float(line.split()[1]))



false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'r',
label='AUC1-5 = %0.2f'% roc_auc)

actual = []
predictions = []
sortroc=open('C:/Users/admin/Desktop/project/step3_trainset/set_6/sortedroc.txt','r').readlines()
for line in sortroc:
    actual.append(float(line.split()[0]))
    predictions.append(float(line.split()[1]))



false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b',
label='AUC6 = %0.2f'% roc_auc)

plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

