from io import StringIO


if __name__ == '__main__':
    f = StringIO()
    f.write("hello\n")
    f.write("hi\n")
    f.write("world!\n")
    print(f.getvalue())

    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())