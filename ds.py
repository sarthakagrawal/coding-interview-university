# design a static array in Python
# array should be initialized with a certain
# length, and have pointers to each element
# stored in the array.


class StaticArray():
    def __init__(self, length):
        self.capacity = length
        self.size = 0
        self.items = list()
        for i in range(length):
            self.items.append(None)

    def push(self, element):
        self.items.append(element)

    def pop(self):
        self.items.pop()

    def at(self, idx):
        return self.items[idx]


thing = {2: "thing"}
