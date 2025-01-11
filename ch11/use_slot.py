class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称



s = Student()
s.name='michael'
s.age = 25
s.score = 99