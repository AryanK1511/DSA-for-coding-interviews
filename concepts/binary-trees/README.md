# Binary Trees

- **Node:** A node is an abstract datatype with two things, data and pointers.
- **Graph:** A graph is a collection of nodes and their pointers to other nodes.
- **Vertices:** The nodes of a graph are called vertices.
- **Tree:** A tree is a type of graph.
- **Root:** The head of a tree is called the root.
- **Binary Tree:** Trees that have at most two children.

## Tree Terminology

- The root node is the node at the "top" of the tree. Every node in the tree is accessible starting from the root node. In most tree questions, the root of the tree will be given as the input, just like how in linked lists, the head was given as the input.
- If you have a node A with an edge to a node B, so A -> B, we call A the parent of node B, and node B a child of node A.
- If a node has no children, it is called a leaf node. The leaf nodes are the leaves of the tree.
- The depth of a node is how far it is from the root node. The root has a depth of 0. Every child has a depth of parentsDepth + 1, so the root's children have a depth of 1, their children have a depth of 2, and so on.
- Lastly, perhaps the most important thing to understand: a subtree of a tree is a node and all its descendants. Trees are recursive - you can treat a subtree as if it was its own tree with the chosen node being the root.

```python
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
```

## Traversing a Tree

The first is called depth-first search (DFS). For binary trees specifically, there are 3 ways to perform DFS - preorder, inorder, and postorder (don't worry though, the type you choose rarely matters). The other main type of traversal is called breadth-first search (BFS). Let's start by looking at DFS.

### Depth-first search (DFS)

In a DFS, we prioritize depth by traversing as far down the tree as possible in one direction (until reaching a leaf node) before considering the other direction.

You can see my implementation of a full binary tree in the [implementation.py](./implementation.py) file.

```python
def dfs(node):
    if node == None:
        return

    dfs(node.left)
    dfs(node.right)
    return
```

#### Pre-order traversal

Current -> Left -> Right

```python
def pot(node):
    if not node:
        return

    print(node.value)
    pot(node.left)
    pot(node.right)
    return
```

#### In-order traversal

Left -> Current -> Right

```python
def iot(node):
    if not node:
        return

    iot(node.left)
    print(node.value)
    iot(node.right)
    return
```

#### Post-order traversal

Left -> Right -> Current

```python
def iot(node):
    if not node:
        return

    iot(node.left)
    iot(node.right)
    print(node.value)
    return
```
