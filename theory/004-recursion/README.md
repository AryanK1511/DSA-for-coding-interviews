# Recursion Introduction

## How function calls work in languages

- While the function is not finished executing, it will remain in stack.
- So your first function call will always stay in the stack until everything else executes and returns.
- When a function finishes executing, it is removed from the stack and the flow of the program is returned to the point where it was called.

> If you are able to create a formula for recursion that is known as recurrence relation

## Recursion Tips

- Try to see if you can break down a problem into smaller problems
- Form the reccurrence relation if needed
- Draw the recursive tree
  - Pay attention to the flow of functions and how they are getting in the stack.
  - Draw the tree and pointers on a pen and paper and also use a debugger to see the tree.
  - See how the values will be returned at each step.
- Find the base condition
- "tail recursion" means that the last statement in a function, is a recursive call to the same function
- Return the recrsive calls if you are expecting a return type

## Working with variables in recursion

- Arguments
  - Whatever you put here is going to go to the next function call
- Return Type
- Body of the function
  - Local variables that are recomputed on every step
