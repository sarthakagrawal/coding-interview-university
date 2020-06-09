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

arr = [1, 4, 5, 6, 64, 87, 89]


def binarySearch(arr, target):
    min, max = 0, len(arr)
    if max < 1:
        return -1
    # first check the middle element. Then see if target is > or < middle
    # element. Recurse.
    midpt = (max + min) // 2
    if arr[midpt] > target:
        binarySearch(arr[min:midpt - 1], target)
    elif arr[midpt] < target:
        binarySearch(arr[midpt + 1:max], target)
    else:
        return midpt
