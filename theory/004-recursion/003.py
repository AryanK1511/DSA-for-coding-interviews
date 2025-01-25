# Basic recursion questions to help build the intuition behind it


def printnumsNto1(n):
    if n == 0:
        return
    print(n)
    printnumsNto1(n - 1)


def printnums1toN(n):
    if n == 0:
        return
    printnums1toN(n - 1)
    print(n)


def productOfNto1(n):
    if n == 1:
        return 1

    return n * productOfNto1(n - 1)
