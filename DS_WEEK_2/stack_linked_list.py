class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked:
    def __init__(self):
        self.top=None
    def is_empty(self):
        return self.top is None
    def push(self,data):
        new_node=Node(data)
        new_node.ref=self.top
        self.top=new_node
    def pop(self):
        if self.is_empty():
            print("empty")
            return None
        popdata=self.top.data
        self.top=self.top.ref
        return popdata
    def show(self):
        if self.is_empty():
            print("empty")
            return None
        current=self.top
        while current:
            print(current.data)
            current=current.ref
        return current
stack=linked()
stack.push(1)
stack.push(2)
stack.show()
print("--after pop__")
stack.pop()
stack.show()


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class linked:
#     def __init__(self):
#         self.top=None
#     def is_empty(self):
#         return self.top is None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.ref=self.top
#         self.top=new_node
#     def pop(self):
#         if self.is_empty():
#             print("empty")
#             return None
#         popdata=self.top.data
#         self.top=self.top.ref
#         return popdata
#     def peek(self):
#         if self.is_empty():
#             print("empty")
#             return None
#         return self.top.data
#     def display(self):
#         current=self.top
#         while current:
#             print(current.data)
#             current=current.ref
#         return current
# stack=linked()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("Stack after pushing elements:")
# stack.display()

# print("Peek:", stack.peek())

# popped_item = stack.pop()
# print("Popped:", popped_item)

# print("Stack after popping an element:")
# stack.display()
