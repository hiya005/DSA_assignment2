class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            print("Value not found")
            return

        current.next = current.next.next
    
    def traverse(self):
        current = self.head
        result = ""

        while current:
            result += str(current.data) + " , "
            current = current.next

        print(f"[{result[:-3]}]" if result else "[]")


def main():
    myList = SinglyLinkedList()  

    myList.insert_at_end(1)
    for i in range(1, 6):
        myList.insert_at_end(i)

    myList.delete_by_value(1)
    myList.traverse()


if __name__ == "__main__":
    main()