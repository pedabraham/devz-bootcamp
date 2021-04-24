class node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None

class stack(object):
    def __init__(self):
        self.head = None
        self.min = None

    def push(self, new_value):

        node2add = node(new_value)
        node2add.next = self.head
        self.head = node2add

        if not self.min:
            new_node = node({'val':node2add.value,'ref':id(node2add)})
            self.min = new_node
        else:
            if node2add.value < self.getMin():
                new_node = node({'val':node2add.value,'ref':id(node2add)})
                new_node.next = self.min
                self.min = new_node

    def pop(self):
        if id(self.head) == self.min.value['ref']:
            self.min = self.min.next

        last_value = self.head.value
        self.head = self.head.next
        return last_value

    def peek(self):
        if not self.head:
            return None
        last_value = self.head.value
        return last_value

    def getMin(self):
        if not self.min:
            return None
        min_value = self.min.value['val']
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
