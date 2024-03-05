class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Empty linked list")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.ref

    def add(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def bubble_sort(self):
        if self.head is None or self.head.ref is None:
            return
        sorted_h=None
        while sorted_h != self.head.ref:
            current=self.head
            

    def bubble_sort(self):
        if self.head is None or self.head.ref is None:
            return

        sorted_tail = None  # To keep track of the sorted part of the list
        while sorted_tail != self.head.ref:
            current = self.head
            while current.ref != sorted_tail:
                if current.data > current.ref.data:
                    # Swap nodes
                    current.data, current.ref.data = current.ref.data, current.data
                current = current.ref
            sorted_tail = current

# Example usage:
LL1 = LinkedList()
LL1.add(90)
LL1.add(4)
LL1.add(3)
LL1.add(8)
LL1.add(9)
LL1.add(6)
LL1.add(1)
LL1.add(0)
LL1.add(-4)
LL1.add(78)

print("Original Linked List:")
LL1.print_LL()

# Sort the linked list using bubble sort
LL1.bubble_sort()

print("\nSorted Linked List:")
LL1.print_LL()
