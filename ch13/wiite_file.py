fpath = 'D:\\error.log'

if __name__ == '__main__':

    # 写入文件
    with open(fpath, 'a', encoding='utf-8') as f:
        f.write('This is a test for IO...')

    # 读取文件
    with open(fpath, 'r', encoding='utf-8') as f:
        s = f.read()
        print(s)