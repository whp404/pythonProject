import base64

def safe_base64_decode(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        return base64.b64decode(s + '=' * (4 - len(s) % 4))

    pass

# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
print(len('abcd '))