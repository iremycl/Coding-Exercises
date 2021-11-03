def revCompDNA(string):
    """
    The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    """
    
    #translate function translates the given string, maketrans function creates a mapping table for replacements.
    comDNA = string.translate(str.maketrans({'A': 'T', 'T': 'A','G': 'C','C': 'G'}))
    revDNA = comDNA[::-1]
    return revDNA

sampleDNA = "AAAACCCGGT"
revCompDNA(sampleDNA)

revc_string = open("rosalind_revc.txt").read().replace("\n","")
print(revc_string)
revCompDNA(revc_string)