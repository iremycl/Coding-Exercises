def hamming_dist(seq1,seq2):
    #Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
    if len(seq1) != len(seq2):
        raise ValueError("Different Sequence lengths")
    c = 0
    for i in range(0,len(seq1)):
        if seq1[i] != seq2[i]:
            c +=1

    return c

seq1, seq2 = open("rosalind_hamm.txt").readlines()

hamming_dist(seq1,seq2)