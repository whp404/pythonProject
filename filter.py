def is_odd(n):
    return n % 2 == 1

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

if __name__ == '__main__':



    list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]));

    f1 =  inc();
    print(f1());
    print(f1());

