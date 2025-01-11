# Press the green button in the gutter to run the script.

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
def nop():
    pass

if __name__ == '__main__':
    #  ========================
    # x = abs(100)
    # y = abs(-20)
    # print(x, y)
    # print('max(1, 2, 3) =', max(1, 2, 3))
    # print('min(1, 2, 3) =', min(1, 2, 3))
    # print('sum([1, 2, 3]) =', sum([1, 2, 3]))

    print(my_abs(-99))

    nop()

    x, y = move(100, 100, 60, math.pi / 6);
    print(x, y);