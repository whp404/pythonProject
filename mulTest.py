def mul(*n):
    if len(n) == 0:    # 首先排除它有可能是个空集，如果是则抛出TypeError
        raise TypeError("参数集不能为空")
    # 如果不为空，则进行连乘
    sum = 1
    for x in n:
        sum *= x
    return sum

# 测试
if __name__ == '__main__':
    print('mul(5) =', mul(5))
    print('mul(5, 6) =', mul(5, 6))
    print('mul(5, 6, 7) =', mul(5, 6, 7))
    print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
    if mul(5) != 5:
        print('mul(5)测试失败!')
    elif mul(5, 6) != 30:
        print('mul(5, 6)测试失败!')
    elif mul(5, 6, 7) != 210:
        print('mul(5, 6, 7)测试失败!')
    elif mul(5, 6, 7, 9) != 1890:
        print('mul(5, 6, 7, 9)测试失败!')
    else:
        try:
            mul()
            print('mul()测试失败!')
        except TypeError:
            print('测试成功!')