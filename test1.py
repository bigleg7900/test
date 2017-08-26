# encoding=utf-8


def test(l):
    l = list(l)
    for i in range(len(l) - 1):
        if l[i] != l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
            if l not in tmp:
                tmp.append(list(l))
                test(l)


if __name__ == '__main__':
    tmp = list()
    list_ = [1, 2, 3]
    tmp.append(list_)
    test(list_)
    print tmp
