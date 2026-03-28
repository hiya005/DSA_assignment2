class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after_node(self, target, value):
        current = self.head

        while current and current.data != target:
            current = current.next

        if current is None:
            print("Value not found")
            return

        new_node = Node(value)

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        else:
            self.tail = new_node

        current.next = new_node

    def delete_at_position(self, pos):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        for i in range(pos):
            if current.next:
                current = current.next
            else:
                print("Invalid position")
                return

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next

        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev

    def display(self):
        current = self.head
        result = []

        while current:
            result.append(str(current.data))
            current = current.next

        print(" <-> ".join(result) if result else "Empty List")


def main():
    my_list = DoublyLinkedList()

    my_list.head = my_list.tail = Node(0)

    for i in range(5):
        my_list.insert_after_node(i, i + 1)

    my_list.display()


if __name__ == "__main__":
    main()