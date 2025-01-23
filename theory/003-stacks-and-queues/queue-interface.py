# Import deque from the collections module
from collections import deque

# Initializing a deque
queue = deque()

# Pushing elements to the queue: Visually they get added from the right
queue.append(1)
queue.append(2)

# Pops the element from the left
queue.popleft()

# Printing the deque and the length of the queue
print(len(queue))
print(queue[-1])
