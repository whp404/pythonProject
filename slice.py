if __name__ == '__main__':
    L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
    print(L[1:3])

    L = list(range(100))
    print(L[::5])

    d = {"a": 1, "b": 2, "c": 3}

    # iter each key:
    print("iter key:", d)
    for k in d.keys():
        print("key:", k)

    # iter each value:
    print("iter value:", d)
    for v in d.values():
        print("value:", v)

    # iter both key and value:
    print("iter item:", d)
    for k, v in d.items():
        print("item:", k, v)
