#!/usr/bin/env python3
'''
Check the main chromosomes (1-22, X, Y) for differences between two builds.
Example usage:
python3 ./compare.py ucsc.hg19.fasta human_g1k_v37.fasta

'''

import sys

def get_sequences(fastafile):
    chroms = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
              '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
              '21', '22', 'X', 'Y']
    # Translation dict from 'chr1' to '1'
    chromdict = dict([("chr"+x, x) for x in chroms])
    seqdict = {"name": fastafile}
    seqname = None
    seqcode = []
    for line in open(fastafile):
        if line.startswith(">"):
            if seqname != None:
                if chromdict.get(seqname, seqname) in chroms:
                    print("...added.")
                    seqdict[seqname] = ''.join(seqcode)
                else:
                    print(f"{chromdict.get(seqname, seqname)} is not in chroms... skipped.")
            newname = line[1:].strip().split(" ")[0]
            seqname = chromdict.get(newname, newname)
            print(f"{line.strip()} | {seqname}")
            seqcode = []
        else:
            seqcode.append(line.strip().upper())
    return seqdict


def doprint(string, operation=['w']):
    print(string)
    with open("compare_out.tsv", operation[0]) as f:
        f.write(string+'\n')
    # Only write the first time, then append (mutable default switcheroo)
    if operation[0] == 'w':
        operation[0] = 'a'


def compare_sequences(seqa, seqb):
    doprint(f"chr\tpos\t{seqa['name']}\t{seqb['name']}")
    for chromname, chroma in seqa.items():
        if chromname != "name":
            chromb = seqb[chromname]
            if len(chroma) != len(chromb):
                doprint(f"Chromosome '{chromname}' has different lengths; comparison skipped, use an alignment tool for this.")
                doprint(f'\t\t{len(chroma)}\t{len(chromb)}')
                continue
            for i in range(len(chroma)):
                if chroma[i] != chromb[i]:
                    doprint(f"{chromname}\t{i+1}\t{chroma[i]}\t{chromb[i]}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <fasta1> <fasta2>")
        sys.exit(1)
    seqa = get_sequences(sys.argv[1])
    seqb = get_sequences(sys.argv[2])
    compare_sequences(seqa, seqb)
