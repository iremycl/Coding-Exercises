def gc_content(seq):
    #Given a DNA seq, 
    A,C,G,T = seq.count("A"),seq.count("C"),seq.count("G"),seq.count("T")
    return round(((C + G) / len(seq) * 100), 5)

gc_content("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")

def gc_test(fastatxt):
    gc_cont = {}
    data = str(fastatxt)

    with open(data, "r+") as a:
        lines = a.readlines()
        for i in range(0,len(lines)):
            if lines[i].startswith(">") == True :
                gc_cont[lines[i].replace(">","").replace("\n","")] = gc_content(lines[i+1]+lines[i+2]+lines[i+3]+lines[i+4])

    max_gc = max(gc_cont, key= lambda x: gc_cont[x])
    print(max_gc.strip())
    return gc_cont.get(max_gc)


gc_test("rosalind_gc.txt")


