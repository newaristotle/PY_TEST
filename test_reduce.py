from functools import reduce

def test(n,m):
    return n+m

print(reduce(test,[1,2,3,4,5,6,7,8,9]))