# Lecture Notes

## table of contents
1. Linked Lists in Python
2. In Class Assignments 

## Linked List in Python

A **linked list** is a linear data structure where elements (called *nodes*) are connected using references, instead of being stored next to each other in memory like a Python list.

---

### Basic Idea
Each node has:
1. **Data** – the value it stores  
2. **Next pointer** – a reference to the next node  

Instead of:
```python
[10, 20, 30]
```

A linked list looks like:
```text
10 → 20 → 30 → None
```

---

### Node Structure in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### Creating a Linked List (Using the Class)

We’ll build the list using **insertion**:

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

### Example Usage

```python
ll = LinkedList()

ll.insert(0, 10)  # 10
ll.insert(1, 20)  # 10 → 20
ll.insert(2, 30)  # 10 → 20 → 30
```

---

### Traversing the List

Traversal means walking through the list from the head to the end:

```python
current = ll.head
while current:
    print(current.data)
    current = current.next
```

Output:
```
10
20
30
```

Traversal is essential because both insertion and deletion rely on reaching the correct position first.

---

### Inserting at a Position

Insert a new node at a specific index (0-based):

```python
def insert(self, position, data):
    new_node = Node(data)

    # Insert at the beginning
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return

    current = self.head
    index = 0

    while current and index < position - 1:
        current = current.next
        index += 1

    if current is None:
        print("Position out of bounds")
        return

    new_node.next = current.next
    current.next = new_node
```

### Example

```python
ll.insert(1, 15)
```

Result:
```
10 → 15 → 20 → 30 → None
```

---

### Deleting by Position

Remove a node at a specific index:

```python
def delete(self, position):
    if not self.head:
        print("List is empty")
        return

    # Delete head
    if position == 0:
        self.head = self.head.next
        return

    current = self.head
    index = 0

    while current.next and index < position - 1:
        current = current.next
        index += 1

    if current.next is None:
        print("Position out of bounds")
        return

    current.next = current.next.next
```

### Example

```python
ll.delete(2)
```

---

### Full Linked List Class

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, position, data):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    def delete(self, position):
        if not self.head:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        index = 0

        while current.next and index < position - 1:
            current = current.next
            index += 1

        if current.next is None:
            print("Position out of bounds")
            return

        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

---

### Key Operations
- **Traverse** (walk through nodes)  
- **Insert** (at position)  
- **Delete** (by position)  

---

### Advantages
- Dynamic size  
- Efficient insertions/deletions  

---

### Disadvantages
- No direct indexing  
- Extra memory for pointers  
- Slower access than Python lists  

---

### Types of Linked Lists
- Singly linked list  
- Doubly linked list  
- Circular linked list  

---

### When to Use
Use linked lists when:
- You frequently insert/delete elements  
- You don’t need fast random access  


## In Class Assignments
### 1. Modify the linked list class above, so that if you only pass the data parameter to the insert method, it inserts the node at the end of the list.
