class node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.min = None

class stack(object):
    def __init__(self):
        self.head = None

    def push(self, new_value):

        new_node = node(new_value)
        new_node.next = self.head

        if not self.head or new_node.value < self.getMin():
            new_node.min = new_node
        else:
            new_node.min = self.head.min

        self.head = new_node


    def pop(self):
        if not self.head:
            return None

        last_value = self.head.value
        self.head = self.head.next
        return last_value

    def peek(self):
        if not self.head:
            return None
        last_value = self.head.value
        return last_value

    def getMin(self):
        if not self.head:
            return None
        min_value = self.head.min.value
        return min_value

new_stack = stack()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
print('push')
new_stack.push(9)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.push(1)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.push(1)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.push(0)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.push(5)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.push(-4)
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')

print('pop')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
new_stack.pop()
print(f'val:{new_stack.peek()} min:{new_stack.getMin()}')
