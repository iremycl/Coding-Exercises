import sys, re
import pandas as pd

def read_fasta(fasta):
    fasta = open(fasta, 'r')
    lines = fasta.readlines()

    hre=re.compile('>(\S+)')
    lre=re.compile('^(\S+)$') # The ^ at the beginning and ' ’ at the end make sure the search string matches the entire line, excluding the terminal newline.

    reads={}

    for line in lines:
        header = hre.search(line) # search for header as defined in hre
        if header:
            id=header.group(1) # \S+ in first bracket
        else:
            seq=lre.search(line)
            if (id in reads.keys()):
                reads[id] += seq.group(1)
            else:
                reads[id] = seq.group(1)
    return reads

fasta="rosalind_cons.txt"
reads=read_fasta(fasta)

def consensus_matrix(reads_dict):
    cm=pd.DataFrame.from_dict(reads_dict,orient='index')
    cm=pd.DataFrame(cm[0].apply(list).tolist())
    cons=cm.mode().head(1).to_string(header=False, index=False).strip().replace(' ', '')
    result={
        'A':[],
        'C':[],
        'G':[],
        'T':[]
    }
    for index,column in cm.iteritems():
        result['A']+=str(len(cm[cm[index] == 'A']))
        result['C']+=str(len(cm[cm[index] == 'C']))
        result['G']+=str(len(cm[cm[index] == 'G']))
        result['T']+=str(len(cm[cm[index] == 'T']))
    print(cons)
    print(('\n'.join("{}: {}".format(k, v) for k, v in result.items())).replace("{","").replace("'","").replace("}","").replace("[","").replace("]","").replace(",",""))

consensus_matrix(reads)
