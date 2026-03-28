import ctypes

class DynamicArray:

    def __init__(self):
        self.size = 0          
        self.capacity = 1      
        self.arr = self.make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return
        return self.arr[index]

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)   
        self.arr[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return

        value = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return value

    def resize(self, new_capacity):
        new_arr = self.make_array(new_capacity)

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
        self.capacity = new_capacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def display(self):
        print("Array:", end=" ")
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print(f"| Size: {self.size} | Capacity: {self.capacity}")



def main():
    arr = DynamicArray()

    for i in range(1, 6):
        arr.append(i)
        arr.display()

    print("Popped:", arr.pop())
    arr.display()

    print("First element:", arr[0])


if __name__ == "__main__":
    main()