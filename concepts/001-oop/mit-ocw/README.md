# Object Oriented Programming in Python by MIT OCW

## Lecture Links

- [Python Classes](https://www.youtube.com/watch?v=tsMrUdynbQQ&list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB&index=17)
- [More Python Class Methods](https://www.youtube.com/watch?v=gLnCmUkgUQk&list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB&index=18)
- [Inheritance](https://www.youtube.com/watch?v=rgM7Z9BNm1s&list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB&index=19)
- [Fitness Tracker Example](https://www.youtube.com/watch?v=-wyc5FwzkcM&list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB&index=20)

## What are Objects?

- Python supports various types of data: **Integers, Floats, Strings, Lists, Dictionaries**, etc.
- Each of these is an **object**. Objects are **data abstractions**, and every object has:
  - **Internal Data Representation**: Can be primitive (e.g., integers) or composite (e.g., lists, dictionaries).
  - **Procedures for Interaction**: Methods or functions to interact with the object.
- An **object** is an **instance of a type**. Examples:
  - `1234` is an instance of `int`.
  - `"Hello"` is an instance of `str`.

## Advantages of Object-Oriented Programming (OOP)

1. **Encapsulation**:

   - Combines **data** and **procedures** into a single package with well-defined interfaces.

2. **Modularity**:

   - Enables **divide-and-conquer development**:
     - Implement and test each class independently.
     - Increased modularity reduces overall complexity.

3. **Code Reusability**:

   - Classes make it easy to **reuse code**:
     - Python modules often define new classes.
     - Each class operates in its own **environment**.
   - **Inheritance**:
     - Allows subclasses to extend or modify the behavior of a superclass.

## Representing a Coordinate in a 2D Plane

- **Concept**: A point in a 2D plane can be represented by:
  - Its distance from the **x-axis** and **y-axis** (x, y coordinates).
  - The distance between two points can be calculated using **Pythagoras' theorem**.

### Defining a Class for Coordinates

```python
class Coordinate:
    """
    A class to represent a 2D coordinate.
    """

    # Special method to initialize attributes
    def __init__(self, xval, yval):
        self.x = xval  # X-coordinate
        self.y = yval  # Y-coordinate
```

- **Attributes**: Data stored in the class (e.g., `x`, `y`).
- **Methods**: Functions that operate on class instances.
  - Use the `self` parameter to refer to the instance of the class.

### Key Notes on Class Definition

- **Dunder Methods**: Special methods in Python prefixed with double underscores (e.g., `__init__`). These have specific purposes, like initialization.
- **Dot Notation**: Access attributes or methods of an object using the dot (`.`) operator.

### Example Method: Calculate Distance

```python
    def distance(self, other):
        """
        Calculate the distance between this coordinate and another.
        """
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
```

- **How it works**:
  - `self`: Refers to the current object.
  - `other`: Another instance of the `Coordinate` class.
