#!/bin/bash
input_dir_svm_files=/home/liu/Desktop/project_data/step5_trainset/radialf/
svm_path=/home/liu/Desktop/svm_light/
for a in 2 8 32; do
	for b in 0.5 2;do
		for i in $input_dir_svm_files/*.svm ; do
			$svm_path/svm_learn -t 2 -c $a -g $b $i.train "${i}${a}${b}".model &>"${i}${a}${b}".learn.log
		done
		for i in $input_dir_svm_files/*.svm ; do
			$svm_path/svm_classify $i "${i}${a}${b}".model "${i}${a}${b}".pred &>"${i}${a}${b}".classify.log
		done
	done
done