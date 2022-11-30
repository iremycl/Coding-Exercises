# Wanted to use KMP Algorithm for this question

def LPSArray(pat):
    """
    We use the LPS table to decide how many characters are to be skipped for comparison when a mismatch has occurred.
    """
    M = len(pat)
    lps = [0]*M
    i = 0 # length of the longest prefix suffix
    j = 1 # starting from jth character of the pattern, not 0.
    while j < M:
        if pat[i] == pat[j]: #Compare the characters at Pattern[i] and Pattern[j]
            lps[j] = i + 1
            i += 1
            j += 1
        else :
            if i != 0: # If the lps is not 0, set it to lps[i-1] and not 0.
                i = lps[i-1]
            else: # If 0, move to the next character.
                j += 1
    return lps

def KMPSearch(pat, txt):
    M = len(txt)
    i = 0 # On text
    j = 0 # On pattern
    lps = LPSArray(pat)
    pattern_index=[]
    while i < M:
        if pat[j] == txt[i]: # Text and pattern matching
            i += 1
            j += 1
            if j == len(pat): # If pattern used up, match found
                pattern_index.append(str(i-j+1))
                j = lps[j-1]
        elif i < M and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return pattern_index

f=open('rosalind_subs.txt')
lines=f.readlines()
txt = lines[0].replace('\n','')
pat = lines[1].replace('\n','')
indices = KMPSearch(pat, txt)
print(*indices, sep=' ')