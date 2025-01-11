def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x
    return counter

def build(x, y):
    return lambda  : x * x + y * y


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
tt=build(1,5)
print(tt())