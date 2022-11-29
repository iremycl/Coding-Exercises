from os import replace


def fib_rabbits(n,k):

    """
    Given: Positive integers n≤40 and k≤5.
    Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
    """
    
    prevA = 0 #Initial number of adult rabbit pairs
    prevB = 1 #Initial number of baby rabbit pairs
    for m in range(1,n):
        total = prevA * k + prevB
        prevA = prevB
        prevB = total
    return total if n != (1 or 2) else prevB



fib_rabbits(5,3)

rabbit_data = open("rosalind_fib.txt").read().replace("\n","")
rabbit_data = [int(i) for i in rabbit_data.split() ]
print(rabbit_data)

fib_rabbits(rabbit_data[0], rabbit_data[1])