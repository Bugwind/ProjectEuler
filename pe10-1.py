from math import sqrt

def primesieve(n):
    '''Sieve of Eratosthenes

Return a list of all primes less than n
'''
    l = range(n)
    l[1]= 0
    for i in range(2, int(sqrt(n)) + 1):
        if l[i]:
            #print ((n - 1 - i**2)//i + 1),
            #print l[i**2::i]
            l[i**2::i] = [0] * ((n - 1 - i**2)//i + 1)

    return [x for x in l if x]

print sum(primesieve(2000000))
