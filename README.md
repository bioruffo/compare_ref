# compare_ref
Simple script to compare two reference fasta files.  

The script will only compare chromosomes that have the same length, so you can use it e.g. to compare UCSC's hg19 reference with human_g1k_v37, but you can't use it to compare a hg19 build vs. a GRCh38 build.  

By default, the script will ignore chrM and any other sequences (decoys etc) that are not chromosomes 1-22, X or Y.

It will print results on screen, and also save them to a file called "compare_out.tsv".  

## Example usage
```
python3 compare.py ucsc.hg19.fasta human_g1k_v37.fasta
```
