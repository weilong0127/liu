#!/bin/bash
input_dir_svm_files=/home/liu/Desktop/project_data/step3_trainset/


for file_i in $input_dir_svm_files/*.svm; do
	for file_j in $input_dir_svm_files/*.svm; do
		if [ $file_i != $file_j ]; then
			cat $file_j >> $file_i.train
		fi
	done
done

