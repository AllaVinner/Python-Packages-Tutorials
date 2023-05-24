GENEFILE="./data/gencommand_proj1_data/apple.genes"

# Get number of gense in a .genes file
cut -f1 $GENEFILE | sort -u | wc -l

# Get number of transcripts
cut -f2 $GENEFILE | sort -u | wc -l

# Get all genes with a single splice variant
cut -f1 $GENEFILE | sort -u | uniq -c | grep -c " 1 "

# Get genes on chromosome 1
cut -f1,3 $GENEFILE | sort -u | cut -f2 | sort | uniq -c

