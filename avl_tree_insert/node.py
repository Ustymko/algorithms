class Node:
    def __init__(self, val: int):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val
        self.max_height = 1
