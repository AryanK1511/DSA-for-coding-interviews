# Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k


def func(arr: list, k: int) -> int:
    left, res, s = 0, 0, 0

    for right in range(len(arr)):
        s += arr[right]
        while s > k:
            s -= arr[left]
            left += 1

        res = max(res, right - left + 1)

    return res


arr = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
print(func(arr, k))
