#!/bin/bash
i=/home/liu/Desktop/project_data/step5_trainset/radialf/set6.svm
svm_path=/home/liu/Desktop/svm_light/


$svm_path/svm_learn -t 2 -c 32 -g 0.5 $i.train "${i}32".model &>"${i}32".learn.log

$svm_path/svm_classify $i "${i}32".model "${i}32".pred &>"${i}32".classify.log