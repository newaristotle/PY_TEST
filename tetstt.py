def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def c():
                return i*i
            return c
        fs.append(f)
    return fs

y=count()
a=y[0]
b=y[1]
c=y[2]
d=a(5)
print(d())

