from functools import reduce
def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name;


def fn(x,y):
    return  x*y

def prod(L):
    return  reduce(fn,L)



if __name__ == '__main__':

    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')



    fs = []
    fs.append(1)
    fs.append(2)
    print(fs)