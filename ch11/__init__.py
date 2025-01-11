from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        if isinstance(gender,Gender):
            self.gender = gender
        else:
            raise ValueError("Gender must be an instance of Gender!")
        self.name = name




if __name__ == '__main__':
    # 测试:
    bart = Student('Bart', Gender.Male)
    if bart.gender == Gender.Male:
        print('测试通过!')
    else:
        print('测试失败!')