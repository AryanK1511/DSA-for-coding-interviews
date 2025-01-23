# Linked Lists

- Linked Lists are just like arrays and they store data in a sequence.
- One difference is that linked lists have pointers so they are not contiguous in memory. Hence, looking for an element is not as simple as just using the index.
- The main advantage is that you can add or remove elements from a linked list in O(1).
- They also have more overhead than arrays since nodes take memory.

## Mechanics of a Linked List

### Assignment

Certainly! Let's break down the provided Python code and understand why the variable `ptr` continues to point to the original `head` node even after modifying `head`.

```python
ptr = head
head = head.next
head = None
```

1. **Initialization:**

   ```python
   ptr = head
   ```

   - Here, `ptr` is assigned the value of `head`. In Python, variables hold references to objects. So, both `ptr` and `head` now reference the **same node** in the linked list.

2. **Moving `head` to the Next Node:**

   ```python
   head = head.next
   ```

   - This line updates `head` to reference the **next node** in the linked list.
   - **Important:** This does **not** affect `ptr`. Since `ptr` was pointing to the original `head`, it continues to reference that original node.

3. **Setting `head` to `None`:**

   ```python
   head = None
   ```

   - This line removes the reference from `head` to any node by setting it to `None`.
   - **Again, this does not affect `ptr`.** `ptr` still holds the reference to the original `head` node because variables in Python hold references independently.

#### Key Concepts to Understand

1. **References in Python:**

   - In Python, variables are references to objects. When you assign `ptr = head`, both variables point to the same object in memory.
   - Changing what `head` points to (like moving it to `head.next` or setting it to `None`) **does not** change where `ptr` points. `ptr` maintains its reference to the original object.

2. **Immutable vs. Mutable Objects:**

   - While this concept primarily applies to data types like integers, strings (immutable) and lists, dictionaries (mutable), in the context of linked lists (which are mutable), changing one reference doesn't inherently affect another reference unless you modify the object itself.
   - In your case, you're not modifying the node's content but merely changing which node `head` references.

3. **Garbage Collection:**

   - If there are no references to an object, Python's garbage collector will reclaim that memory. However, since `ptr` still references the original `head` node, it won't be garbage collected.
   - Setting `head` to `None` removes one reference, but as long as `ptr` references the node, it remains accessible.

#### Visualization

Let's visualize the references to make it clearer.

1. **Initial State:**

   ```txt
   head --> [Node1] --> [Node2] --> [Node3] --> None
   ```

2. **After `ptr = head`:**

   ```txt
   ptr  --> [Node1] --> [Node2] --> [Node3] --> None
   head --> [Node1] --> [Node2] --> [Node3] --> None
   ```

3. **After `head = head.next`:**

   ```ptr
   ptr  --> [Node1] --> [Node2] --> [Node3] --> None
   head --> [Node2] --> [Node3] --> None
   ```

4. **After `head = None`:**

   ```txt
   ptr  --> [Node1] --> [Node2] --> [Node3] --> None
   head  --> None
   ```

- **Final State:** `ptr` still points to `[Node1]`, the original head, even though `head` has been moved forward and then set to `None`.

## Traversal

### Iterative

```python
def get_sum(head):
    sum = 0
    while head:
        sum += head.val
        head = head.next
    return sum
```

### Recursive

```python
def get_sum(head):
    if not head:
        return 0

    return head.val + get_sum(head.next)
```

## Types of Linked Lists

### Singly Linked Lists

Each node only has a pointer to the next node.

```python
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def addNode(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

def delete_node(prev_node):
    prev_node.next = prev_node.next.next
```

## Doubly Linked List

A doubly linked list is a single linked list, but with each node also containing a pointer to the previous node.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_node(node, node_to_add):
    prev_node = node.prev
    node_to_add.next = node
    node_to_add.prev = prev_node
    prev_node.next = node_to_add
    node.prev = node_to_add

def delete_node(node):
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node
```

## Linked Lists with Sentinel Nodes

We call the start of the list, `head` and the end is called `tail`. The idea behind linked lists with Sentinel nodes is that even if there are no nodes in a linked lists, we do not have to handle that explicitly. So the real head is actually `head.next` and the real tail is actually `tail.prev` but these nodes make operations cleaner.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add

def remove_from_end():
    if head.next == tail:
        return

    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return

    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head = ListNode(None)
tail = ListNode(None)
head.next = tail
tail.prev = head
```

## Using Dummy Pointers

We usually want to reference the head to ensure we can always access any element. Sometimes, it is better to traverse using a "dummy" pointer and to keep head at the head.

```python
def get_sum(head):
    ans = 0
    dummy = head

    while dummy:
        ans += dummy.value
        dummy = dummy.next

    return ans
```
