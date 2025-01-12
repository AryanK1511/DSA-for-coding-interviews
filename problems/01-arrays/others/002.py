# Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise.


def func(nums: list, target: int) -> bool:
    left, right = 0, len(nums)

    while left < right:
        if left + right > target:
            right -= 1
        elif left + right < target:
            left += 1
        else:
            return True

    return False


nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(func(nums, target))
