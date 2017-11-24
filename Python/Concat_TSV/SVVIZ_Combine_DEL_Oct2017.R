################################
# Date: October 11 2017
# Revised dataframe merge c("Ill300x.GT","Ill250.GT","IllMP.GT","TenX.GT","pacbio.GT")
# Will adjust genotype label for each technology
# Adapted from Justin Zook
################################

install.packages("reshape")
library(reshape)
library(ggplot2)
library(data.table)

#Ill 6kb MP
AJMP <- data.frame()
for(i in c(1:1000)) {
  if (file.exists(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizMPAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"))) {
    tmp1<-read.table(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizMPAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"), header = TRUE, sep = "\t", na.strings = c("NA", NA, "NaN"))
    if (nrow(tmp1)>0) {
      tmp1$id<-i #<- id corresponds with line # in svviz input VCF
      AJMP <- rbind(AJMP,tmp1)
    }
  }
}

head(AJMP, n=5)
AJMPcast <- cast(AJMP,variant + sample + key + id ~ allele,fill=0)
AJMPb <- AJMP[,c(1:2,6)]
AJMPb$sample <- ifelse(AJMPb$sample=="HG002_mate_pair","HG002",ifelse(AJMPb$sample=="HG003_mate_pair","HG003","HG004"))
AJMPb$allelekey <- with(AJMP, paste(allele,key,sep='_'))
AJMPb$value <- AJMP[,5]
AJMPcastall <- cast(AJMPb,variant + sample + id ~ allelekey,fill=0)
colnames(AJMPcastall)[c(-1,-2,-3)] <- paste0("IllMP.",colnames(AJMPcastall)[c(-1,-2,-3)])
AJMPcastall$type <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall$variant),'::chr'), "[", 1)),':'), "[", 1)
AJMPcastall$chrom <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall$variant),'::chr'), "[", 2)),':'), "[", 1)
AJMPcastall$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 1)))
AJMPcastall[is.na(AJMPcastall$start),]$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall[is.na(AJMPcastall$start),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))
AJMPcastall$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),'\\('), "[", 1)))
AJMPcastall[is.na(AJMPcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall[is.na(AJMPcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),';'), "[", 1)))
AJMPcastall[is.na(AJMPcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJMPcastall[is.na(AJMPcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))-1
AJMPcastall$IllMP.GT <- ifelse(AJMPcastall$IllMP.alt_count>20 & AJMPcastall$IllMP.ref_count>20,1,ifelse(AJMPcastall$IllMP.alt_count>40 & AJMPcastall$IllMP.ref_count<10,2,ifelse(AJMPcastall$IllMP.alt_count<10 & AJMPcastall$IllMP.ref_count>40,0,-1)))
#write.csv(AJMPcastall, row.names = FALSE, file = "/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame1/DEL/4001-5000/MPtest.DEL.csv")
AJMPcastall.DEL <- read.csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame2-PythonOutput/DEL/4001-5000/MP.DEL.csv")
sum(AJMPcastall.DEL[AJMPcastall.DEL$sample=="HG002",]$IllMP.GT==-1)
sum(AJMPcastall.DEL[AJMPcastall.DEL$sample=="HG002",]$IllMP.GT==0)
sum(AJMPcastall.DEL[AJMPcastall.DEL$sample=="HG002",]$IllMP.GT==1)
sum(AJMPcastall.DEL[AJMPcastall.DEL$sample=="HG002",]$IllMP.GT==2)
ggplot(AJMPcastall.DEL, aes(x=log10(IllMP.ref_count), y=log10(IllMP.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJMPcast[AJMPcast$key=="count",], aes(x=log10(ref))) +  geom_histogram(binwidth=0.1,colour="white")
ggplot(AJMPcast[AJMPcast$key=="count",], aes(x=log10(alt))) +  geom_histogram


#Ill 300x 150bp
AJ300x <- data.frame()
for(i in c(1:1000)) {
  if (file.exists(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizIll300xAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"))) {
    tmp1<-read.table(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizIll300xAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"), header = TRUE, sep = "\t", na.strings = c("NA", NA, "NaN"))
    if (nrow(tmp1)>0) {
      tmp1$id<-i
      AJ300x <- rbind(AJ300x,tmp1)
    }
  }
}
head(AJ300x, n=5)
AJ300xcast <- cast(AJ300x,variant + sample + key + id ~ allele,fill=0)
AJ300xb <- AJ300x[,c(1:2,6)]
AJ300xb$sample <- ifelse(AJ300xb$sample=="HG002_hs37d5_300x","HG002",ifelse(AJ300xb$sample=="HG003_hs37d5_300x","HG003","HG004"))
AJ300xb$allelekey <- with(AJ300x, paste(allele,key,sep='_'))
AJ300xb$value <- AJ300x[,5]
AJ300xcastall <- cast(AJ300xb,variant + sample + id ~ allelekey,fill=0)
colnames(AJ300xcastall)[c(-1,-2,-3)] <- paste0("Ill300x.",colnames(AJ300xcastall)[c(-1,-2,-3)])
AJ300xcastall$type <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall$variant),'::'), "[", 1)),':'), "[", 1)
AJ300xcastall$chrom <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall$variant),'::'), "[", 2)),':'), "[", 1)
AJ300xcastall$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 1)))
AJ300xcastall[is.na(AJ300xcastall$start),]$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall[is.na(AJ300xcastall$start),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))
AJ300xcastall$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),'\\('), "[", 1)))
AJ300xcastall[is.na(AJ300xcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall[is.na(AJ300xcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),';'), "[", 1)))
AJ300xcastall[is.na(AJ300xcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ300xcastall[is.na(AJ300xcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))-1
AJ300xcastall$Ill300x.GT <- ifelse(AJ300xcastall$Ill300x.alt_count>75 & AJ300xcastall$Ill300x.ref_count>75,1,ifelse(AJ300xcastall$Ill300x.alt_count>100 & AJ300xcastall$Ill300x.ref_count<5,2,ifelse(AJ300xcastall$Ill300x.alt_count<5 & AJ300xcastall$Ill300x.ref_count>100,0,-1)))
#write.csv(AJ300xcastall, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame1/DEL/4001-5000/300xtest.DEL.csv")
AJ300xcastall.DEL <- read.csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame2-PythonOutput/DEL/4001-5000/300x.DEL.csv")
sum(AJ300xcastall.DEL[AJ300xcastall.DEL$sample=="HG002",]$Ill300x.GT==-1)
sum(AJ300xcastall.DEL[AJ300xcastall.DEL$sample=="HG002",]$Ill300x.GT==0)
sum(AJ300xcastall.DEL[AJ300xcastall.DEL$sample=="HG002",]$Ill300x.GT==1)
sum(AJ300xcastall.DEL[AJ300xcastall.DEL$sample=="HG002",]$Ill300x.GT==2)
ggplot(AJ300xcastall.DEL, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))  + facet_grid(SVtype ~ .)
ggplot(AJ300xcast[AJ300xcast$key=="count",], aes(x=log10(ref))) +  geom_histogram(binwidth=0.1,colour="white")
ggplot(AJ300xcast[AJ300xcast$key=="count",], aes(x=log10(alt))) +  geom_histogram(binwidth=0.1,colour="white")

#Ill 250bp
AJ250bp <- data.frame()
for(i in c(1:1000)) {
  if (file.exists(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizIll250bpAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"))) {
    tmp1<-read.table(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizIll250bpAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"), header = TRUE, sep = "\t", na.strings = c("NA", NA, "NaN"))
    if (nrow(tmp1)>0) {
      tmp1$id<-i
      AJ250bp <- rbind(AJ250bp,tmp1)
    }
  }
}
AJ250bpcast <- cast(AJ250bp,variant + sample + key + id ~ allele,fill=0)
AJ250bpb <- AJ250bp[,c(1:2,6)]
AJ250bpb$sample <- ifelse(AJ250bpb$sample=="HG002_hs37d5_2x250","HG002",ifelse(AJ250bpb$sample=="HG003_hs37d5_2x250","HG003","HG004"))
AJ250bpb$allelekey <- with(AJ250bp, paste(allele,key,sep='_'))
AJ250bpb$value <- AJ250bp[,5]
AJ250bpcastall <- cast(AJ250bpb,variant + sample + id ~ allelekey,fill=0)
colnames(AJ250bpcastall)[c(-1,-2,-3)] <- paste0("Ill250.",colnames(AJ250bpcastall)[c(-1,-2,-3)])
AJ250bpcastall$type <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall$variant),'::'), "[", 1)),':'), "[", 1)
AJ250bpcastall$chrom <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall$variant),'::'), "[", 2)),':'), "[", 1)
AJ250bpcastall$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 1)))
AJ250bpcastall[is.na(AJ250bpcastall$start),]$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall[is.na(AJ250bpcastall$start),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))
AJ250bpcastall$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),'\\('), "[", 1)))
AJ250bpcastall[is.na(AJ250bpcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall[is.na(AJ250bpcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),';'), "[", 1)))
AJ250bpcastall[is.na(AJ250bpcastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ250bpcastall[is.na(AJ250bpcastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))-1
AJ250bpcastall$Ill250.GT <- ifelse(AJ250bpcastall$Ill250.alt_count>10 & AJ250bpcastall$Ill250.ref_count>10,1,ifelse(AJ250bpcastall$Ill250.alt_count>20 & AJ250bpcastall$Ill250.ref_count<3,2,ifelse(AJ250bpcastall$Ill250.alt_count<3 & AJ250bpcastall$Ill250.ref_count>20,0,-1)))
#write.csv(AJ250bpcastall, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame1/DEL/4001-5000/250bptest.DEL.csv")
AJ250bpcastall.DEL <- read.csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame2-PythonOutput/DEL/4001-5000/250bp.DEL.csv")
sum(AJ250bpcastall.DEL[AJ250bpcastall.DEL$sample=="HG002",]$Ill250.GT==-1)
sum(AJ250bpcastall.DEL[AJ250bpcastall.DEL$sample=="HG002",]$Ill250.GT==0)
sum(AJ250bpcastall.DEL[AJ250bpcastall.DEL$sample=="HG002",]$Ill250.GT==1)
sum(AJ250bpcastall.DEL[AJ250bpcastall.DEL$sample=="HG002",]$Ill250.GT==2)
ggplot(AJ250bpcastall.DEL, aes(x=log10(Ill250.ref_count), y=log10(Ill250.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJ250bpcast[AJ250bpcast$key=="count",], aes(x=log10(ref))) +  geom_histogram(binwidth=0.1,colour="white")
ggplot(AJ250bpcast[AJ250bpcast$key=="count",], aes(x=log10(alt))) +  geom_histogram(binwidth=0.1,colour="white")

# pacbio
AJpacbio <- data.frame()
for(i in c(1:1000)) {
  if (file.exists(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizPacBioAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"))) {
    tmp1<-read.table(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svvizPacBioAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"), header = TRUE, sep = "\t", na.strings = c("NA", NA, "NaN"))
    if (nrow(tmp1)>0) {
      tmp1$id<-i
      AJpacbio <- rbind(AJpacbio,tmp1)
    }
  }
}
AJpacbiocast <- cast(AJpacbio,variant + sample + key + id ~ allele,fill=0)
AJpacbiob <- AJpacbio[,c(1:2,6)]
AJpacbiob$sample <- ifelse(AJpacbiob$sample=="BWA-MEM_HG002_merged_11_12","HG002",ifelse(AJpacbiob$sample=="BWA-MEM_HG003_merged_11_12","HG003","HG004"))
AJpacbiob$allelekey <- with(AJpacbio, paste(allele,key,sep='_'))
AJpacbiob$value <- AJpacbio[,5]
AJpacbiocastall <- cast(AJpacbiob,variant + sample + id ~ allelekey,fill=0)
colnames(AJpacbiocastall)[c(-1,-2,-3)] <- paste0("pacbio.",colnames(AJpacbiocastall)[c(-1,-2,-3)])
AJpacbiocastall$type <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall$variant),'::'), "[", 1)),':'), "[", 1)
AJpacbiocastall$chrom <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall$variant),'::'), "[", 2)),':'), "[", 1)
AJpacbiocastall$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 1)))
AJpacbiocastall[is.na(AJpacbiocastall$start),]$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall[is.na(AJpacbiocastall$start),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))
AJpacbiocastall$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),'\\('), "[", 1)))
AJpacbiocastall[is.na(AJpacbiocastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall[is.na(AJpacbiocastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),';'), "[", 1)))
AJpacbiocastall[is.na(AJpacbiocastall$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJpacbiocastall[is.na(AJpacbiocastall$end),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))-1
AJpacbiocastall$pacbio.GT <- ifelse(AJpacbiocastall$pacbio.alt_count>4 & AJpacbiocastall$pacbio.ref_count>4,1,ifelse(AJpacbiocastall$pacbio.alt_count>9 & AJpacbiocastall$pacbio.ref_count<1,2,ifelse(AJpacbiocastall$pacbio.alt_count<1 & AJpacbiocastall$pacbio.ref_count>9,0,-1)))
#write.csv(AJpacbiocastall, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame1/DEL/4001-5000/PacBiotest.DEL.csv")
AJpacbiocastall.DEL <- read.csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame2-PythonOutput/DEL/4001-5000/PacBio.DEL.csv")
sum(AJpacbiocastall.DEL[AJpacbiocastall.DEL$sample=="HG002",]$pacbio.GT==-1)
sum(AJpacbiocastall.DEL[AJpacbiocastall.DEL$sample=="HG002",]$pacbio.GT==0)
sum(AJpacbiocastall.DEL[AJpacbiocastall.DEL$sample=="HG002",]$pacbio.GT==1)
sum(AJpacbiocastall.DEL[AJpacbiocastall.DEL$sample=="HG002",]$pacbio.GT==2)
ggplot(AJpacbiocastall.DEL, aes(x=log10(pacbio.ref_count), y=log10(pacbio.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJpacbiocastall.DEL[AJpacbiocastall.DEL$key=="count",], aes(x=log10(ref))) +  geom_histogram(binwidth=0.1,colour="white")
ggplot(AJpacbiocastall.DEL[AJpacbiocastall.DEL$key=="count",], aes(x=log10(alt))) +  geom_histogram(binwidth=0.1,colour="white")

#10X by haplotype
AJ10X <- data.frame()
for(i in c(1:1000)) {
  if (file.exists(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svviz10XAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"))) {
    tmp1<-read.table(paste0("/Volumes/lesleydata/SVVIZOutput/April112017/Step1/SVVIZ/SVVIZoutput/DEL/4001-5000/svviz10XAJTrioDEL2/summary_union_refalt.sort.DEL.4001to5000_",i,".tsv"), header = TRUE, sep = "\t", na.strings = c("NA", NA, "NaN"))
    if (nrow(tmp1)>0) {
      tmp1$id<-i
      AJ10X <- rbind(AJ10X,tmp1)
    }
  }
}
AJ10Xcast <- cast(AJ10X,variant + sample + key + id ~ allele,fill=0)
AJ10Xb <- AJ10X[,c(1,5,6)]
AJ10Xb$sample <- sapply(strsplit(as.character(AJ10X$sample),'_GRCh37_'), "[", 1)
AJ10Xb$sample <- ifelse(AJ10Xb$sample=="NA24385","HG002",ifelse(AJ10Xb$sample=="NA24149","HG003","HG004"))
AJ10Xb$HP <- sapply(strsplit(as.character(AJ10X$sample),'_GRCh37_'), "[", 2)
AJ10Xb$allelekey <- with(AJ10X, paste(allele,key,sep='_'))
AJ10Xcastall.DEL <- cast(AJ10Xb,variant + sample + id ~ HP + allelekey,fill=0)
colnames(AJ10Xcastall.DEL)[c(-1,-2,-3)] <- paste0("TenX.",colnames(AJ10Xcastall.DEL)[c(-1,-2,-3)])
AJ10Xcastall.DEL$type <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL$variant),'::chr'), "[", 1)),':'), "[", 1)
AJ10Xcastall.DEL$chrom <- sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL$variant),'::chr'), "[", 2)),':'), "[", 1)
AJ10Xcastall.DEL$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 1)))
AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$start),]$start <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$start),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))
AJ10Xcastall.DEL$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),'\\('), "[", 1)))
AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$end),]$variant),'::'), "[", 2)),':'), "[", 2)),'-'), "[", 2)),';'), "[", 1)))
AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$end),]$end <- as.numeric(gsub(",", "", sapply(strsplit(as.character(sapply(strsplit(as.character(sapply(strsplit(as.character(AJ10Xcastall.DEL[is.na(AJ10Xcastall.DEL$end),]$variant),'::'), "[", 2)),':'), "[", 2)),';'), "[", 1)))-1
AJ10Xcastall.DEL$TenX.GT <- ifelse((AJ10Xcastall.DEL$TenX.HP1_alt_count>5 & AJ10Xcastall.DEL$TenX.HP1_ref_count<2 & AJ10Xcastall.DEL$TenX.HP2_alt_count<2 & AJ10Xcastall.DEL$TenX.HP2_ref_count>5) | (AJ10Xcastall.DEL$TenX.HP2_alt_count>5 & AJ10Xcastall.DEL$TenX.HP2_ref_count<2 & AJ10Xcastall.DEL$TenX.HP1_alt_count<2 & AJ10Xcastall.DEL$TenX.HP1_ref_count>5),1,ifelse((AJ10Xcastall.DEL$TenX.HP1_alt_count>5 & AJ10Xcastall.DEL$TenX.HP1_ref_count<2 & AJ10Xcastall.DEL$TenX.HP2_alt_count>5 & AJ10Xcastall.DEL$TenX.HP2_ref_count<2),2,ifelse((AJ10Xcastall.DEL$TenX.HP1_alt_count<2 & AJ10Xcastall.DEL$TenX.HP1_ref_count>5 & AJ10Xcastall.DEL$TenX.HP2_alt_count<2 & AJ10Xcastall.DEL$TenX.HP2_ref_count>5),0,-1)))
#write.csv(AJ10Xcastall.DEL, file= '/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame1/DEL/4001-5000/10xtest.DEL.csv', row.names = FALSE)
AJ10Xcastall.DEL <- read.csv("/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame2-PythonOutput/DEL/4001-5000/10x.DEL.csv")
sum(AJ10Xcastall.DEL[AJ10Xcastall.DEL$sample=="HG002",]$TenX.GT==-1)
sum(AJ10Xcastall.DEL[AJ10Xcastall.DEL$sample=="HG002",]$TenX.GT==0)
sum(AJ10Xcastall.DEL[AJ10Xcastall.DEL$sample=="HG002",]$TenX.GT==1)
sum(AJ10Xcastall.DEL[AJ10Xcastall.DEL$sample=="HG002",]$TenX.GT==2)
ggplot(AJ10Xcastall.DEL, aes(x=log10(TenX.HP1_ref_count), y=log10(TenX.HP2_alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJ10Xcastall.DEL, aes(x=log10(TenX.HP1_ref_count), y=log10(TenX.HP1_alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJ10Xcast[AJ10Xcast$key=="count",], aes(x=log10(ref))) +  geom_histogram(binwidth=0.1,colour="white")
ggplot(AJ10Xcast[AJ10Xcast$key=="count",], aes(x=log10(alt))) +  geom_histogram(binwidth=0.1,colour="white")


#merge all technologies
#DTAJ300xcastall.DEL <- data.table(AJ300xcastall.DEL[,c("chrom","start","end","sample","id","SVtype","Ill300x.GT","Size")], key='chrom,start,end,sample,id,SVtype,Size')
#DTAJ250bpcastall.DEL <- data.table(AJ250bpcastall.DEL[,c("chrom","start","end","sample","id","SVtype","Ill250.GT", "Size")], key='chrom,start,end,sample,id,SVtype,Size')
#DTAJMPcastall.DEL <- data.table(AJMPcastall.DEL[,c("chrom","start","end","sample","id","SVtype","IllMP.GT", "Size")], key='chrom,start,end,sample,id,SVtype,Size')
#DTAJpacbiocastall.DEL <- data.table(AJpacbiocastall.DEL[,c("chrom","start","end","sample","id","SVtype","pacbio.GT", "Size")], key='chrom,start,end,sample,id,SVtype,Size')
#DT10Xcastall.DEL <- data.table(AJ10Xcastall.DEL[,c("chrom","start","end","sample","id","SVtype","TenX.GT", "Size")], key='chrom,start,end,sample,id,SVtype,Size')
#AJmerge <- data.frame(Reduce(function(...) merge(..., all=TRUE, by=c("chrom","start","end","sample","id","SVtype", "Size")), list(DTAJ300xcastall,DTAJ250bpcastall.DEL,DTAJMPcastall,DTAJpacbiocastall,DT10Xcastall)))
#AJmerge <- data.frame(Reduce(function(...) merge(..., all=TRUE, by=c("chrom","start","end","sample","id","SVtype", "Size")), list(DTAJ300xcastall.DEL,DTAJ250bpcastall.DEL,DTAJMPcastall.DEL,DT10Xcastall.DEL,DTAJpacbiocastall.DEL)))


#Creates exported file with all features from technologies(datasets) for machine learning
DTAJ300xcastall.DEL <- data.table(AJ300xcastall.DEL[,2:(ncol(AJ300xcastall.DEL))], key='chrom,start,end,sample,id,type,SVtype,Size')
DTAJ250bpcastall.DEL <- data.table(AJ250bpcastall.DEL[,2:(ncol(AJ250bpcastall.DEL))], key='chrom,start,end,sample,id,type,SVtype,Size')
DTAJMPcastall.DEL <- data.table(AJMPcastall.DEL[,2:(ncol(AJMPcastall.DEL))], key='chrom,start,end,sample,id,type,SVtype,Size') 
DTAJpacbiocastall.DEL <- data.table(AJpacbiocastall.DEL[,2:(ncol(AJpacbiocastall.DEL))], key='chrom,start,end,sample,id,type,SVtype,Size')
DT10Xcastall.DEL <- data.table(AJ10Xcastall.DEL[,2:(ncol(AJ10Xcastall.DEL))], key='chrom,start,end,sample,id,type,SVtype,Size')
AJmergeallcol.DEL <- data.frame(Reduce(function(...) merge(..., all=TRUE, by=c("chrom","start","end","sample","id","type","SVtype","Size")), list(DTAJ300xcastall.DEL,DTAJ250bpcastall.DEL,DTAJMPcastall.DEL,DT10Xcastall.DEL,DTAJpacbiocastall.DEL)))
AJmerge <- merge(AJpacbiocastall[,c("chrom","start","end","sample","id","pacbio.GT")],merge(AJ10Xcastall.DEL[,c("chrom","start","end","sample","id","TenX.GT")],merge(AJ250bpcastall.DEL[,c("chrom","start","end","sample","id","Ill250.GT")],merge(AJMPcastall.DEL[,c("chrom","start","end","sample","id","IllMP.GT")],AJ300xcastall.DEL[,c("chrom","start","end","sample","id","Ill300x.GT")],by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".MP",".300x")),by = c("chrom","start","end","sample","id"), all=TRUE),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".10X",".250bp")),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".pacbio",""))
#AJmergeallcol <- data.frame(Reduce(function(...) merge(..., all=TRUE, by=c("chrom","start","end","sample","id","type","SVtype","Size")), list(DTAJ300xcastall,DTAJ250bpcastall,DTAJMPcastall,DTAJpacbiocastall,DT10Xcastall)))
#AJmergewithcnts <- merge(AJpacbiocastall[,c("chrom","start","end","sample","id","pacbio.GT")],merge(AJ10Xcastall[,c("chrom","start","end","sample","id","TenX.GT","HP1_ref_count","HP1_alt_count","HP2_ref_count","HP2_alt_count")],merge(AJ250bpcastall[,c("chrom","start","end","sample","id","GT","ref_count","alt_count")],merge(AJMPcastall[,c("chrom","start","end","sample","id","GT","ref_count","alt_count")],AJ300xcastall[,c("chrom","start","end","sample","id","GT","ref_count","alt_count")],by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".MP",".300x")),by = c("chrom","start","end","sample","id"), all=TRUE),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".10X",".250bp")),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".pacbio",""))
#AJmergeallcol <- merge(AJpacbiocastall[,2:(ncol(AJpacbiocastall)-1)],merge(AJ10Xcastall[,2:(ncol(AJ10Xcastall)-1)],merge(AJ250bpcastall[,2:(ncol(AJ250bpcastall)-1)],merge(AJMPcastall[,2:(ncol(AJMPcastall)-1)],AJ300xcastall[,2:(ncol(AJ300xcastall)-1)],by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".MP",".300x")),by = c("chrom","start","end","sample","id"), all=TRUE),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".10X",".250bp")),by = c("chrom","start","end","sample","id"), all=TRUE, suffixes = c(".pacbio",""))

AJmendelian300x.DEL <- cast(DTAJ300xcastall.DEL,chrom+start+end+id+SVtype ~ sample,value="Ill300x.GT")
write.csv(AJmendelian300x.DEL, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame3-MendelianOutput/DEL/4001-5000/300xMendelian.DEL.4001-5000.csv")
AJmendelian250x.DEL <- cast(DTAJ250bpcastall.DEL,chrom+start+end+id+SVtype ~ sample,value="Ill250.GT")
write.csv(AJmendelian250x.DEL, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame3-MendelianOutput/DEL/4001-5000/250xMendelian.DEL.4001-5000.csv")
AJmendelianMP.DEL <- cast(DTAJMPcastall.DEL,chrom+start+end+id+SVtype ~ sample,value="IllMP.GT")
write.csv(AJmendelianMP.DEL, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame3-MendelianOutput/DEL/4001-5000/MPMendelian.DEL.4001-5000.csv")
AJmendelianPacBio.DEL <- cast(DTAJpacbiocastall.DEL,chrom+start+end+id+SVtype ~ sample,value="pacbio.GT")
write.csv(AJmendelianPacBio.DEL, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame3-MendelianOutput/DEL/4001-5000/PacBioMendelian.DEL.4001-5000.csv")
AJmendelian10x.DEL <- cast(DT10Xcastall.DEL,chrom+start+end+id+SVtype ~ sample,value="TenX.GT")
write.csv(AJmendelian10x.DEL, row.names = FALSE, file ="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame3-MendelianOutput/DEL/4001-5000/10xMendelian.DEL.4001-5000.csv")

#AJmerge$size <- AJmerge$end - AJmerge$start
AJmerge$GTcons <- -1
AJmerge$GTconflict <- -1
AJmerge$GTsupp <- 0
for(i in c(1:nrow(AJmerge))) {
  gt1=-1
  n=0
  conflict=0
  for(j in c("Ill300x.GT","Ill250.GT","IllMP.GT","TenX.GT","pacbio.GT")) {
    #for(j in c(8:9)) {
    if(!is.na(AJmerge[i,j]) & AJmerge[i,j]>-1) {
      if(gt1==-1) {
        gt1=AJmerge[i,j]
        n=n+1
      } else {
        if (gt1==AJmerge[i,j]) {n=n+1} else {conflict=conflict+1}
      }
    }
  }
  if(conflict==0) {
    AJmerge[i,"GTcons"]=gt1
    AJmerge[i,"GTsupp"]=n
  } else {
    AJmerge[i,"GTconflict"]=1
  }
}
sum(AJmerge$GTcons==-1)
sum(AJmerge$GTconflict==1)
sum(AJmerge$GTcons==0)
sum(AJmerge$GTcons==1)
sum(AJmerge$GTcons==2)
sum(AJmerge$GTcons==0 & AJmerge$GTsupp>1)
sum(AJmerge$GTcons==1 & AJmerge$GTsupp>1)
sum(AJmerge$GTcons==2 & AJmerge$GTsupp>1)
sum(AJmerge$GTcons==0 & AJmerge$GTsupp==5)
sum(AJmerge$GTcons==1 & AJmerge$GTsupp==5)
sum(AJmerge$GTcons==2 & AJmerge$GTsupp==5)

AJmergeallcol.DEL <- cbind(AJmergeallcol.DEL,AJmerge[,11:13])
write.table(AJmergeallcol.DEL,file="/Volumes/lesleydata/SVVIZOutput/April112017/Step2/R-GenerateBedFile/DataFrame4-ML.BedFile/DEL/4001-5000/svvizAllData.DEL.4001-5000.bed", row.names=FALSE, col.names=TRUE, quote=FALSE, sep = "\t")

contingencytable <- xtabs(~TenX.GT+Ill300x.GT+Ill250.GT+IllMP, data=AJmerge)
ftable(contingencytable,row.vars=c(2:4))

AJmergetrio <- cast(AJmerge,chrom+start+end+id+SVtype ~ sample,value="GTcons")

contingencytable <- xtabs(~HG004+HG003+HG002, data=AJmergetrio)
ftable(contingencytable,row.vars=c(1,2))

#merge with input bed file
#bed <- read.table("/Users/lmc2/Desktop/NIST/Data/Dec72016.svvizData/tech_filt.bed", header = FALSE, sep = "\t", na.strings = c("NA", NA, "NaN"))
#bed$chrom <- sapply(strsplit(as.character(bed$V1),'chr'), "[", 2)
#mergebed <- merge(bed,AJmergetrio,by.x=c("chrom","V2","V3"),by.y = c("chrom","start","end"))

#contingency table of genotype vs # of technologies supporting it
#contingencytable2 <- xtabs(~V6+HG002, data=mergebed)
#ftable(contingencytable2)

#contingency table of genotype vs # of callsets supporting it
#contingencytable3 <- xtabs(~V7+HG002, data=mergebed)
#ftable(contingencytable3)

#sites from >5 callsets determined to be hom ref
#mergebed[mergebed$HG002==0 & mergebed$V7>5,]

#write.table(mergebed,file="/Users/lmc2/Desktop/NIST/Data/Dec72016.svvizData/filtremain_svvizGT.bed", row.names=FALSE, col.names=FALSE, quote=FALSE, sep = "\t")



#merge consensus GT back with original tables from each dataset
#PacBio
AJmergepacbio <- merge(AJpacbiocastall,AJmerge,by = c("chrom","start","end","sample","id"))
ggplot(AJmergepacbio, aes(x=log10(pacbio.ref_count), y=log10(pacbio.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJmergepacbio, aes(x=log10(pacbio.ref_count), y=log10(pacbio.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ pacbio.GT.x ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(pacbio.ref_count), y=log10(pacbio.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ pacbio.GT.x ~ GTconflict)
ggplot(AJmergepacbio, aes(x=log10(pacbio.ref_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(pacbio.alt_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(pacbio.amb_count-pacbio.amb_reason_flanking))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(pacbio.ref_count), y=log10(end-start))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(abs(Size.x)), y=log10(pacbio.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(abs(Size.x)), y=log10(pacbio.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergepacbio, aes(x=log10(abs(Size.x)), y=log10(pacbio.alt_count/pacbio.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)

#300x
AJmerge300x <- merge(AJ300xcastall.DEL,AJmerge,by = c("chrom","start","end","sample","id"))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTconflict)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.alt_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.amb_count-Ill300x.amb_reason_flanking))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(end-start))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(abs(Size.x)), y=log10(Ill300x.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(abs(Size.x)), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(abs(Size.x)), y=log10(Ill300x.alt_count/Ill300x.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)

#10X
AJmerge10X <- merge(AJ10Xcastall.DEL,AJmerge,by = c("chrom","start","end","sample","id"))
ggplot(AJmerge10X, aes(x=TenX.HP1_alt_count/(TenX.HP1_alt_count+TenX.HP1_ref_count), y=TenX.HP2_alt_count/(TenX.HP2_alt_count+TenX.HP2_ref_count))) +  geom_point(shape=1, position=position_jitter(width=.01,height=.01))
ggplot(AJmerge10X, aes(x=TenX.HP1_alt_count/(TenX.HP1_alt_count+TenX.HP1_ref_count), y=TenX.HP2_alt_count/(TenX.HP2_alt_count+TenX.HP2_ref_count))) +  geom_point(shape=1, position=position_jitter(width=.01,height=.01)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge10X, aes(x=TenX.HP1_alt_count/(TenX.HP1_alt_count+TenX.HP1_ref_count), y=TenX.HP2_alt_count/(TenX.HP2_alt_count+TenX.HP2_ref_count))) +  geom_point(shape=1, position=position_jitter(width=.01,height=.01)) + facet_grid(sample ~ TenX.GT.x ~ GTconflict)
ggplot(AJmerge10X, aes(x=TenX.HP1_alt_count/(TenX.HP1_alt_count+TenX.HP1_ref_count))) +  geom_histogram(binwidth=0.05,colour="white") + facet_grid(. ~ GTcons)
ggplot(AJmerge10X, aes(x=TenX.HP2_alt_count/(TenX.HP2_alt_count+TenX.HP2_ref_count))) +  geom_histogram(binwidth=0.05,colour="white") + facet_grid(. ~ GTcons)
ggplot(AJmerge10X, aes(x=(TenX.HP1_alt_count))) +  geom_histogram(binwidth=1,colour="black") + facet_grid(. ~ GTcons)
ggplot(AJmerge10X, aes(x=(TenX.HP1_alt_count+TenX.HP2_alt_count))) +  geom_histogram(binwidth=1,colour="black") + facet_grid(sample ~ GTcons)
ggplot(AJmerge10X, aes(x=log10(TenX.HP1_amb_count-TenX.HP1_amb_reason_flanking+TenX.HP2_amb_count-TenX.HP2_amb_reason_flanking))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(. ~ GTcons)
ggplot(AJmerge10X, aes(x=log10(TenX.HP1_ref_count+TenX.HP2_ref_count), y=log10(end-start))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(. ~ GTcons)
ggplot(AJmerge10X, aes(x=log10(abs(Size.x)), y=log10(TenX.HP2_ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge10X, aes(x=log10(abs(Size.x)), y=log10(TenX.HP2_alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge10X, aes(x=log10(abs(Size.x)), y=log10(TenX.HP2_alt_count/TenX.HP2_ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)

#250x
AJmerge250x <- merge(AJ250bpcastall.DEL,AJmerge,by = c("chrom","start","end","sample","id"))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTconflict)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.alt_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.amb_count-Ill300x.amb_reason_flanking))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(end-start))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge250x, aes(x=log10(abs(Size.x)), y=log10(Ill250.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge250x, aes(x=log10(abs(Size.x)), y=log10(Ill250.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmerge250x, aes(x=log10(abs(Size.x)), y=log10(Ill250.alt_count/Ill250.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)


#MP
AJmergeMP <- merge(AJMPcastall.DEL,AJmerge,by = c("chrom","start","end","sample","id"))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03))
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(Ill300x.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(Ill300x.GT.x ~ GTconflict)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.alt_count))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.amb_count-Ill300x.amb_reason_flanking))) +  geom_histogram(binwidth=0.1,colour="white") + facet_grid(sample ~ GTcons)
ggplot(AJmerge300x, aes(x=log10(Ill300x.ref_count), y=log10(end-start))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergeMP, aes(x=log10(abs(Size.x)), y=log10(IllMP.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergeMP, aes(x=log10(abs(Size.x)), y=log10(IllMP.alt_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
ggplot(AJmergeMP, aes(x=log10(abs(Size.x)), y=log10(IllMP.alt_count/IllMP.ref_count))) +  geom_point(shape=1, position=position_jitter(width=.03,height=.03)) + facet_grid(sample ~ GTcons)
