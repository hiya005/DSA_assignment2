class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stacksinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print("Stack is empty")
            return

        value = self.head.data        
        self.head = self.head.next
        return value
        
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return

        return self.head.data
    
    def traverse(self):
        if self.head is None:
            print("[ ]")
            return

        current = self.head
        result = ""

        while current:
            result += str(current.data) + " , "
            current = current.next

        print(f"[{result[:-3]}]")


def main():
    myStack = stacksinglyLinkedList()   

    for i in range(1, 6):
        myStack.push(i)

    print(myStack.pop())
    print(myStack.peek())
    myStack.traverse()


if __name__ == "__main__":
    main()