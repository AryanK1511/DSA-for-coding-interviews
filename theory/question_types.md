# Some Common Patterns and Techniques to solve questions

## Binary Trees

### Using DFS vs BFS

When you need to visit each node, use DFS. BFS makes sense if you need to handle the nodes according to their level. DFS is easier to implement with less code so choose DFS when it doesn't matter if you use BFS or DFS.

The main disadvantage of DFS is that you could end up wasting a lot of time looking for a value. Let's say that you had a huge tree, and you were looking for a value that is stored in the root's right child. If you do DFS prioritizing left before right, then you will search the entire left subtree, which could be hundreds of thousands if not millions of operations. Meanwhile, the node is literally one operation away from the root. The main disadvantage of BFS is that if the node you're searching for is near the bottom, then you will waste a lot of time searching through all the levels to reach the bottom.

DFS uses space linear with the height of the tree. BFS uses space linear with the level that has the most nodes. In a perfect binary tree, DFS would use O(logn) whereas BFS would use O(n)

## Arrays

### Two pointers

#### Method 1

1. Start the pointers at the edges of the input and move them towards each other until they meet.
2. So basically, left start at `0` and right starts at `input.length - 1`.
3. Use a while loop until the pointers are equal to each other
4. At each iteration increment the left pointer and decrement the right pointer.

#### Method 2

1. Move along both inputs simultaneously until all elements have been checked.
2. Create two pointers, one for each iterable.
3. Use a while loop until one of the iterables reaches the end
4. Sometimes the size of both inputs might not be the same so you will have to iterate through each one individually as well later.

### Sliding Window

Basically, a good rule of thumb is, whenever you see the word subarray, think about using sliding windows at least once.

Use this approach when:

1. You see subarrays and you have to find the number of valid ones somehow.
2. Number of valid subarrays
   1. The number of valid windows ending at index right is equal to the size of the window, which we know is right - left + 1
   2. When we say "the number of valid subarrays ending at index right is equal to the size of the window (right - left + 1)," this is specifically referring to subarrays that end at the current index right. If you're considering all valid subarrays in the entire array (not just those ending at a particular index), the total count involves summing up these contributions for each index right.
3. Fixed window size

Here is some pseudocode and most of the questions look like this.

```txt
function fn(nums, k):
    left = 0
    curr = 0
    answer = 0
    for (int right = 0; right < nums.length; right++):
        curr += nums[right]
        while (curr > k):
            curr -= nums[left]
            left++

        answer = max(answer, right - left + 1)

    return answer
```

Sliding windows will make 2n iterations since the left pointer will move at most n times and the right pointer will move at most n times as well. Which means that a sliding window algorithm runs in O(n) time usually.

### Prefix Sum

Prefix sum is the idea of creating a prefix sum array where `prefix[i]` is the sum of all elements up to the index `i` (inclusive).

```txt
arr = [1, 2, 3, 4]
prefix_sum = [1, 3, 6, 10]
```

**When to use:**

- Range sums
- Sliding window like computations
- Repeated Computations

**Math:**

Let us say I want to calculate the sum of subarray from `i` to `j`. It would be defined as `prefix[j] - prefix[i] + arr[i]` (If we handle the index being 0 edge case) otherwise it will be `prefix[j] - prefix[i - 1]`.

### More Common Patterns

#### String Building

- **Challenges**: Strings are immutable in most languages, leading to $O(n^2)$ complexity with repeated concatenation.
- **Optimized Approaches**:

  1. **Python**: Use a list and join.

     ```python
     def build_string(s):
         arr = []
         for c in s:
             arr.append(c)
         return "".join(arr)
     ```

     **Time Complexity**: \(O(n)\).

  2. **Java**: Use `StringBuilder`.

     ```java
     public String buildString(String s) {
         StringBuilder sb = new StringBuilder();
         for (int i = 0; i < s.length(); i++) {
             sb.append(s.charAt(i));
         }
         return sb.toString();
     }
     ```

     **Time Complexity**: \(O(n)\).

- **C++ and JavaScript**: Simply using `+=` works efficiently.

#### Subarrays, Subsequences, and Subsets

##### **Subarrays/ Substrings**

- **Definition**: Contiguous sections of an array or string.
- **Patterns**:
  - Sliding Window: Useful for constraints like sum \(>k\), max length, or number of unique elements.
  - Prefix Sum: Optimize multiple range sum calculations.

#### **Subsequences**

- **Definition**: A set of elements keeping the same relative order (not necessarily contiguous).
- **Key Points**:
  - Order matters.
  - Common pattern: Two Pointers (especially with two arrays/strings).
- **Example**: Subsequence of `[1, 2, 3, 4]` includes `[1, 3]`, `[4]`, `[]`.

#### **Subsets**

- **Definition**: Any set of elements from the array, where order doesn’t matter.
- **Key Points**:
  - Use sorting if order doesn’t matter.
  - Backtracking often used to generate subsets.
- **Example**: Subsets of `[1, 2, 3]` include `[1, 2]`, `[3]`, `[]`.
