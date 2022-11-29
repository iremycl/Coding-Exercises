def mendel(k,m,n):
    """
    Given three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    Return the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
    """
    # Calculate the probability of genotype aa, which can be the result of ddxdd, Ddxdd or DdxDd matings: 
    total = k+m+n
    tworecessive = ((n/total)*((n-1)/(total-1))) # All of the offspring will have aa genotype.
    onerecessive = (((n/total)*(m/(total-1)))+((n/(total-1))*(m/(total)))) *.5 #Only half of the offspring of this pair will have aa genotype, other half will have Aa.
    twohetero = (((m/total)*((m-1)/(total-1)))) *.25 #Only 1/4 of the offspring of this pair will have aa genotype.
                
    return 1-(tworecessive + onerecessive + twohetero)


mendel(2,2,2)

with open ("rosalind_iprb.txt", "r") as file:
    line =file.readline().split()
    k, m, n= [int(n) for n in line]
    print(k, m, n)
file.close()
print(mendel(k, m, n))

# 19 20 15
# 0.7886093640810622