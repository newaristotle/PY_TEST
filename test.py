import functools

def fib(name):
    k=name[0].upper()
    for i in range(1,len(name)):
        k=k+name[i]
    return k

r=map(fib,['sda','sdasd','erewr','wetrgfd'])
z=list(r)
print(z)

