from color import Color


class Node:
    def __init__(self, val):
        self.val = val
        self.color = Color.Red
        self.left = None
        self.right = None
        self.parent = None
