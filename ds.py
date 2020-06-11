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


class binary_search_tree_node():
    def __init__(self, val, parent=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

    def find_node_to_append(self, target):
        if target > self.val:
            if self.right is not None:
                self.right.find_node_to_append(target)
            else:
                return (self, "right")
        elif target < self.val:
            if self.left is not None:
                self.left.find_node_to_append(target)
            else:
                return (self, "left")
        else:
            return self

    def insert_node(self, target):
        # node = self.find_node_to_append(val)
        # node[0].node[1].left = binary_search_tree_node(val, node[0])
        if target > self.val:
            if self.right is not None:
                self.right.insert_node(target)
            else:
                self.right = binary_search_tree_node(target, self)
        elif target < self.val:
            if self.left is not None:
                self.left.insert_node(target)
            else:
                self.left = binary_search_tree_node(target, self)
        else:
            return "Error, node already exists."

    def delete_node(self, target):
        if target > self.val:
            if self.right is not None:
                self.right.delete_node(target)
            else:
                return "Error, node does not exist."
        elif target < self.val:
            if self.left is not None:
                self.left.delete_node(target)
            else:
                return "Error, node does not exist."
        else:
            if self.left is None or self.right is None:
                if self.val > self.parent.val:
                    self.parent.right = self.right
                    self.parent.right.left = self.left
                else:
                    self.parent.left = self.left
                    self.parent.left.right = self.right
            else:
                curr = self
                while curr.left.left is not None:
                    curr = curr.left
                    self.val = curr.val
                    self.right.delete_node(self.val)

    def in_order_traversal(self):
        self.left.in_order_traversal() if self.left else None
        print(self.val)
        self.right.in_order_traversal() if self.right else None


a = binary_search_tree_node(4)
lst = [56, 25, 75, 57, 89, 24, 45]
for item in lst:
    a.insert_node(item)

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
