def power(x):
    return x*x

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


def calc(numbers):
    sum = 0
    for n in numbers:
        sum+=n
    return sum

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, job):
    print(name, age, city, job)


if __name__ == '__main__':

    # print(power(5,3));
    # enroll('Sarah', 'F');
    # enroll('Adam', 'M', city='Tianjin')
    #
    # print(calc([1, 2, 3]))
    # print(calc1(1, 2, 3))

    person('Jack', 24, city='Beijing', job='Engineer')
