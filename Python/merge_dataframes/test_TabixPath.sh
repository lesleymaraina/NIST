#!/bin/sh
#SBATCH -p owners
#SBATCH --array=1-2
#SBATCH -o genosv_pass_%A_%a.out
#SBATCH -e genosv_pass_%A_%a.err
#SBATCH --cpus-per-task=4
#SBATCH -t 00-12:00:00
#SBATCH -A msalit

#SBATCH --mem=16000

head -"${SLURM_ARRAY_TASK_ID}"0 /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/practice_1.vcf | tail -10 > /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/union_refalt.sort.DEL.1001to2000_nochr_"${SLURM_ARRAY_TASK_ID}".vcf

cat /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/header_2.vcf /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/union_refalt.sort.DEL.1001to2000_nochr_"${SLURM_ARRAY_TASK_ID}".vcf | bgzip -c > /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/genosv_test/Dec222017/vcf."${SLURM_ARRAY_TASK_ID}".vcf.gz

/home/users/lmc2/htslib/bin/tabix /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/genosv_test/Dec222017/vcf."${SLURM_ARRAY_TASK_ID}".vcf.gz

genosv --also-plot-context 4000 --outdir svvizgenosvPB --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/lmc2/AJTrio/svvizconfirm/union_161111/genosv_test/Dec222017/vcf."${SLURM_ARRAY_TASK_ID}".vcf.gz  /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_PB_70x.bam,sequencer=pacbio
genosv --outdir svvizgenosvIll150bp --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/jzook/AJTrio/svvizconfirm/AJTrio_svviz_random5000_170509/manualcuration_examples.vcf.gz /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_Ill_150bp_300x.bam
genosv --outdir svvizgenosvIll250bp --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/jzook/AJTrio/svvizconfirm/AJTrio_svviz_random5000_170509/manualcuration_examples.vcf.gz /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_Ill_250bp_45x.bam
genosv --outdir svvizgenosv10X --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/jzook/AJTrio/svvizconfirm/AJTrio_svviz_random5000_170509/manualcuration_examples.vcf.gz  /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_10X_86x_HP1.bam /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_10X_86x_HP2.bam
genosv --outdir svvizgenosvIllMP --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/jzook/AJTrio/svvizconfirm/AJTrio_svviz_random5000_170509/manualcuration_examples.vcf.gz /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_Ill_6kbMP_15x.bam 
genosv --align-distance 10000 --also-plot-context 4000 --outdir svvizgenosvPB10Xassembly --ref /oak/stanford/groups/msalit/shared/genomes/hg19/hg19.fasta  -V /scratch/PI/msalit/jzook/AJTrio/svvizconfirm/AJTrio_svviz_random5000_170509/manualcuration_examples.vcf.gz /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_PB_10X_assembly_HP1.bam /oak/stanford/groups/msalit/shared/giab/hg19/HG002/HG002_PB_10X_assembly_HP2.bam





