# Some Common Patterns and Techniques to solve questions

## Two pointers

### Method 1

1. Start the pointers at the edges of the input and move them towards each other until they meet.
2. So basically, left start at `0` and right starts at `input.length - 1`.
3. Use a while loop until the pointers are equal to each other
4. At each iteration increment the left pointer and decrement the right pointer.

### Method 2

1. Move along both inputs simultaneously until all elements have been checked.
2. Create two pointers, one for each iterable.
3. Use a while loop until one of the iterables reaches the end
4. Sometimes the size of both inputs might not be the same so you will have to iterate through each one individually as well later.
