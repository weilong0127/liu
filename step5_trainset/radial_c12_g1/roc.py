j=1
while j<=2:
    ii=1
    w=open('roc'+str(j)+'1.txt','w+')
    while ii<=5:
        setname=open('set'+str(ii)+'.svm','r').read().splitlines()
        predname=open('set'+str(ii)+'.svm'+str(j)+'1.pred','r').read().splitlines()
        for n in range(len(setname)):
                
                w.write(setname[n][:2]+' '+predname[n]+'\n')
        ii=ii+1
    w.close()
    lines=open('roc'+str(j)+'1.txt','r').read().splitlines()
    ww=open('sortedroc'+str(j)+'1.txt','w+')
    for li in sorted(lines, key=lambda line:float(line.split()[1])):
        ww.write(li+'\n')
    ww.close()
    i=0
    j=j+1


from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
dict={0:'r',1:'y',2:'g',3:'b'}
dict2={0:'linear: ', 1:'polynomial: ', 2:'RBF: ', 3:'sigmoid: '}
i=1
while i<=2:
    actual = []
    predictions = []
    sortroc=open('sortedroc'+str(i)+'1.txt','r').readlines()
    for line in sortroc:
        actual.append(float(line.split()[0]))
        predictions.append(float(line.split()[1]))
    false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
    roc_auc = auc(false_positive_rate, true_positive_rate)
    plt.plot(false_positive_rate, true_positive_rate, dict[i], label=dict2[i]+'%0.4f'% roc_auc)
    plt.plot([0,1],[0,1],'r--')
    plt.xlim([-0.1,1.2])
    plt.ylim([-0.1,1.2])
    i=i+1
plt.legend(loc='lower right')
plt.title('Receiver Operating Characteristic')

plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

