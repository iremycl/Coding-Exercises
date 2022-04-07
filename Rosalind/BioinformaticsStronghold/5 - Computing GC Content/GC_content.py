def gc_content(seq):
    """
    Given one DNA seq, calculate the GC content.
    """
    A,C,G,T = seq.count("A"),seq.count("C"),seq.count("G"),seq.count("T")
    return round(((C + G) / (A+C+G+T) * 100), 5)

#A quick example for the above function
gc_content("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

#Create empty dictionary to hold gc contents
def gc_test(fastatxt):
    """
    Given a file with many reads, calculate the GC content of each read
    """
    gc_cont = {}#Create empty dictionary to hold gc contents
    data = str(fastatxt) 
    with open(data, "r+") as a:
        lines = a.readlines()
        for i in range(0,len(lines)): #read line by line
            if lines[i].startswith(">") == True: #if line starts with >, save as key. 
                if i != 0:
                    gc_cont[key] = gc_content(seq) #When the next sequence starts, save the previous in the dictionary, take the new line as key and reset the seq string
                key = str(lines[i].replace(">","").replace("\n",""))
                seq = ""
            else:
                seq += str(lines[i]) #if not, add line to the string
                if i == len(lines)-1: #Add the last sequence
                    gc_cont[key] = gc_content(seq)
        print(gc_cont)
    
    max_gc = max(gc_cont, key= lambda x: gc_cont[x])
    print(max_gc.strip())
    return gc_cont.get(max_gc)


gc_test("rosalind_gc.txt")
