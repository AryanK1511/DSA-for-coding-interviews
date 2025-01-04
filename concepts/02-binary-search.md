# Binary Search Notes

- **Binary Search** is an efficient algorithm for finding an item from a sorted list of items.
- It works by repeatedly dividing the search interval in half.
- If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half. Otherwise, it continues in the upper half.
- It has a time complexity of **O(log n)**, which makes it much faster than linear search (O(n)) for large datasets.

## Preconditions

- The list (or array) **must be sorted** for Binary Search to work.
- Binary Search can be applied on **sorted arrays** or **sorted linked lists**.

## Steps for Binary Search

1. **Initialize the boundaries**: Start with two pointers, `low` and `high`, representing the start and end of the list (or array).
2. **Find the middle element**: Calculate the middle index using:
   $$
   \text{mid} = \text{low} + \frac{\text{high} - \text{low}}{2}
   $$
3. **Compare the middle element** with the target:
   - If the target equals the middle element, the search is successful, and the index is returned.
   - If the target is less than the middle element, update `high` to `mid - 1` to search the lower half.
   - If the target is greater than the middle element, update `low` to `mid + 1` to search the upper half.
4. **Repeat** steps 2 and 3 until the target is found or the `low` pointer exceeds the `high` pointer (meaning the target is not in the list).

## Example Code (Python)

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            high = mid - 1

        # If target is larger, ignore the left half
        else:
            low = mid + 1

    return -1  # Target not found
```

## Key Concepts

- **Time Complexity**:
  - **Best case**: O(1) (when the middle element is the target).
  - **Worst case**: O(log n) (repeated halving of the search space).
- **Space Complexity**: O(1) for iterative implementations. Recursive implementations may require O(log n) space due to the recursion stack.

## Variants of Binary Search

1. **First Occurrence**: Find the index of the first occurrence of a target element in a sorted array.
2. **Last Occurrence**: Find the index of the last occurrence of a target element.
3. **Search for Closest Value**: Find the closest element in a sorted array to the given target.

## Binary Search on Sorted Linked List

- In a sorted linked list, you can perform binary search, but finding the middle element takes O(n) time (since you have to traverse to it).
- For a linked list, a more suitable method could be **Tortoise and Hare** or **Jump Search**.

## When to Use Binary Search

- **Finding an element** in a sorted collection.
- **Finding boundaries** (e.g., first or last occurrence).
- **Searching for a value** satisfying a certain condition, like finding the smallest or largest number that meets a certain criteria.

## Benefits

- **Efficiency**: Binary search is much faster than linear search for large datasets, especially with time complexity O(log n).
- **Simple to implement**: With a clear structure, binary search can be coded efficiently.

## Binary Search (Search Range Variation)

Imagine you picked a number from 1 to 100 and asked your friend to guess the number you were thinking of. There are three possible outcomes:

- The guess is **correct**.
- The guess is **too small**.
- The guess is **too large**.

After every guess, you would tell them if their guess was correct, too small, or too large. Your friend would then adjust their next guess accordingly.

At its core, this is a binary search problem. As long as there is a way to determine if the number is too big, too small, or correct, we can adjust the search space accordingly.

In many problems, comparing the guess to the target is done by a predefined function or some mathematical equation. For example, consider the function `isCorrect(n)` that returns:

- `1` if `n` is too big,
- `-1` if `n` is too small,
- `0` if `n` is correct.

```python
# Return 1 if n is too big, -1 if too small, 0 if correct
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
```

We can now use this function to implement binary search. We calculate the middle of the search space and pass it to the `isCorrect` function as our guess. Depending on the return value, we adjust our search space accordingly.

```python
# Binary search on some range of values
def binarySearch(low, high):

    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1
```

## Time and Space Complexity

- **Time Complexity**: O(log n), where `n` is the size of the search space.
- **Space Complexity**: O(1), as no additional space is used.
