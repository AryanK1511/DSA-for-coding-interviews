# Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.


def func(arr1: list, arr2: list) -> list:
    i1, i2 = 0, 0
    arr = []

    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            arr.append(arr1[i1])
            i1 += 1
        else:
            arr.append(arr2[i2])
            i2 += 1

    while i1 < len(arr1):
        arr.append(arr1[i1])
        i1 += 1

    while i2 < len(arr2):
        arr.append(arr2[i2])
        i2 += 1

    return arr


arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 6]
print(func(arr1, arr2))
