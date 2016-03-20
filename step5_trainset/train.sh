#!/bin/bash
input_dir_svm_files=/home/liu/Desktop/project_data/step5_trainset/
svm_path=/home/liu/Desktop/svm_light/

for n in `seq 0 4` ; do
	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_learn -t $n $i.train "${i}${n}".model 
	done

	for i in $input_dir_svm_files/*.svm ; do
		$svm_path/svm_classify $i "${i}${n}".model "${i}${n}".pred
	done
done