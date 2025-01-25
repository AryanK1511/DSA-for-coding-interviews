def binarySearch(arr, target):
    def helper(s, e):
        if s > e:
            return -1

        m = s + ((e - s) // 2)

        if arr[m] > target:
            return helper(s, m - 1)
        elif arr[m] < target:
            return helper(m + 1, e)
        else:
            return m

    return helper(0, len(arr) - 1)


print(binarySearch([2, 4, 5, 6, 8, 9, 13, 17, 24], 4))
