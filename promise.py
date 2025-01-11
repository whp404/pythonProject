def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
        print(i)
    return fs


def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


if __name__ == '__main__':
    f1,_,_= count();
    print("================");
    f11, f12, f13 = count1()
    print(f11())
    print(f12())
    print(f13())
