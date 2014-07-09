#coding:utf-8

#找出一个数的分解 返回一个生成器
def primefactors(n):
    '''Generate all prime factors of n.'''
    f = 2
    while f * f <= n:
        while not n % f:
            yield f
            n //= f
        f += 1
    if n > 1:
        yield n

from collections import defaultdict

def groupcount(sq):
    ''' Accept a sequence, sq, and count its elements by group '''
    d   = defaultdict(int)  # default 0
    for each in sq:
        d[each] += 1
    return dict(d)

def uniprimefact(n):
    ''' Return the Unique Prime-Factorization representation of n 
    
    let n = (a**x) * (b**y) * (c**z) * ...
    return {a: x, b: y, c: z, ...}
    '''

    return groupcount(primefactors(n))


from itertools import *
def trinum(n):
    ''' Return the n-th triangle number '''
    return n*(n+1)/2

def trinumgen():
    ''' Generate the sequence of triangle numbers '''
    for n in count(1):
        yield trinum(n)

        
def product(s):
    return reduce(lambda x,y:x*y, s, 1)

for trin in trinumgen():
    if product(each + 1 for each in uniprimefact(trin).values()) > 500:
        print trin
        break
