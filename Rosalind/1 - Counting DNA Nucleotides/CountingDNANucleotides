def count_nucleotides(string):
    """
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    #Get all the characters uppercase
    string = string.upper()
    #Create empty dictionary
    dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for n in string:
        dict[n] += 1
    counts = print(dict['A']," ",dict['C']," ", dict['G']," ",dict['T'])
    return  counts

count_nucleotides("AAAATGTGTgctgCTGCTGT")

ex_string = open("rosalind_dna.txt").read().replace('\n','')
print(ex_string)
count_nucleotides(ex_string)
