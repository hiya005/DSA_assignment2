class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class queuesingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return

        value = self.head.data
        self.head = self.head.next

        if self.head is None:   # queue becomes empty
            self.tail = None

        return value
        
    def display(self):
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
    myQueue = queuesingleLinkedList()   

    for i in range(1, 6):
        myQueue.enqueue(i)

    myQueue.display()

    myQueue.dequeue()
    myQueue.display()
    

if __name__ == "__main__":
    main()