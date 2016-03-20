#!/bin/bash
input_dir_svm_files=/home/liu/Desktop/project_data/step3_trainset/
svm_path=/home/liu/Desktop/svm_light/


for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_learn $i.train $i.model 
done

for i in $input_dir_svm_files/*.svm ; do
	$svm_path/svm_classify $i $i.model $i.pred
done