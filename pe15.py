def memoized(f):
    '''Memoization decorator for referentially transparent function.'''
    m = {} # storage for key -> value pair
    l = lambda *k: m[k] if k in m else m.setdefault(k, f(*k))
    l.cached = m
    return l

@memoized
def a(x, y):
    if (x==0 or y==0):
        return 1
    else:
        return a(x-1, y) + a(x, y-1)

print a(20, 20)
