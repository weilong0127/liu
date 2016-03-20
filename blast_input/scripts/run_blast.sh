path_input_files=/home/liu/Desktop/project_data/blast_input/
path_output_files=/home/liu/Desktop/project_data/step4_blast_output/
path_uniref90=/home/liu/Desktop/uniref90_files/uniref90.fasta
for i in $path_input_files/*.fasta ; do
	base=`basename $i .fasta`
	if [ ! -f $path_output_files/$base.psi ] ; then
		blastpgp -a 3 -j 3 -d $path_uniref90 -i $i -o $path_output_files/$base.blastpgp -Q $path_output_files/$base.psi &>$path_output_files/$base.log
	fi
done
