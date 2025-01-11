"""
实现如下调用:
GET /users/:user/repos
调用时，需要把:user替换为实际用户名
Chain().users('michael').repos
"""
class Chain(object):

    def __init__(self, path=""):
        print(f"__init__ : {path}")
        self._path = path

    def __call__(self, user):
        print(f"__call__ : {self._path} || {user}")
        return Chain("%s/%s" % (self._path, user))

    def __getattr__(self, path):
        print(f"__getattr__ : {self._path} || {path}")
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        print(f"__str__ : {self._path}")
        return self._path

    def __repr__(self):
        print(f"__repr__ : {self._path}")
        return self._path

    # __repr__ = __str__


# 调用顺序:
# __init__ :
# __getattr__ :  || users
# __init__ : /users
# __call__ : /users || michael
# __init__ : /users/michael
# __getattr__ : /users/michael || repos
# __init__ : /users/michael/repos
# __str__ : /users/michael/repos
print(Chain().users("michael").repos)

# 调用顺序:
# __init__ : test
# __getattr__ : test || users
# __init__ : test/users
# __call__ : test/users || michael
# __init__ : test/users/michael
# __getattr__ : test/users/michael || repos
# __init__ : test/users/michael/repos
# __str__ : test/users/michael/repos
print(Chain("test").users("michael").repos)