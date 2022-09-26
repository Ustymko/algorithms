from typing import Optional

from color import Color


class Node:
    def __init__(self, val):
        self.val = val
        self.color = Color.Red
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self, root: Node):
        self.root = root

    def transplant(self, higher_node: Node, shorter_node: Node):
        if higher_node.parent:
            shorter_node.parent = higher_node.parent
            if higher_node.val < higher_node.parent.val:
                higher_node.parent.left = shorter_node
            else:
                higher_node.parent.right = shorter_node
        else:
            if shorter_node.val:
                self.root = shorter_node
        shorter_node.parent = higher_node.parent

    def left_rotate(self, father: Node, child: Node, grandfather: Optional[Node]):
        father.right = child.left
        father.parent = child
        child.left = father
        child.parent = grandfather
        if grandfather:
            if child.val < grandfather.val:
                grandfather.left = child
            else:
                grandfather.right = child
        else:
            if child.val:
                self.root = child

    def right_rotate(self, father: Node, child: Node, grandfather: Optional[Node]):
        father.left = child.right
        father.parent = child
        child.right = father
        child.parent = grandfather
        if grandfather:
            if child.val < grandfather.val:
                grandfather.left = child
            else:
                grandfather.right = child
        else:
            if child.val:
                self.root = child

    def delete_node(self, node_to_be_deleted: Node):
        original_color = node_to_be_deleted.color
        if node_to_be_deleted.left.val is None:
            x = node_to_be_deleted.right
            # self.transplant(node_to_be_deleted, x)
            x.val, node_to_be_deleted.val = node_to_be_deleted.val, x.val

        elif node_to_be_deleted.right.val is None:
            x = node_to_be_deleted.left
            x.val, node_to_be_deleted.val = node_to_be_deleted.val, x.val
            # self.transplant(node_to_be_deleted, x)
        else:
            temp = node_to_be_deleted.left
            y = temp
            while temp.val is not None:
                y = temp
                temp = temp.right
            original_color = y.color
            x = y.right
            if y.parent is node_to_be_deleted:
                x.parent = y
            else:
                y.val, y.right.val = y.right.val, y.val
                # self.transplant(y, y.right)
            if y.left.val is not None:
                y.parent.right = y.left
            else:
                y.parent.right = None
            y.right = node_to_be_deleted.right
            y.left = node_to_be_deleted.left
            y.parent = node_to_be_deleted.parent
            if node_to_be_deleted is self.root:
                self.root = y
            original_color = y.color

        if original_color is Color.Black:
            self.fix_colors(x)

        if self.root.color is Color.Red:
            self.root.color = Color.Black

    def fix_colors(self, current: Node):
        while current is not self.root and current.color is Color.Black:
            if current is current.parent.left:
                w = current.parent.right

                # CASE 1
                if current.parent.right.color is Color.Red:
                    current.parent.right.color = Color.Black
                    current.parent.color = Color.Red
                    self.left_rotate(current.parent, current, current.parent.parent)
                    w = current.parent.right

                # CASE 2
                elif w.left.color is Color.Black and w.right.color is Color.Black:
                    w.color = Color.Red
                    current = current.parent

                # CASE 3
                elif w.right.color is Color.Black:
                    w.left.color = Color.Black
                    w.color = Color.Red
                    self.right_rotate(w, w.left, w.parent)
                    w = current.parent.right

                # CASE 4
                else:
                    w.color = current.parent.color
                    current.parent.color = Color.Black
                    w.right.color = Color.Black
                    self.left_rotate(current.parent, current.parent.right, current.parent.parent)
                    if current.val is not None:
                        self.root = current
            else:
                w = current.parent.left

                # CASE 1
                if current.parent.left.color is Color.Red:
                    current.parent.left.color = Color.Black
                    current.parent.color = Color.Red
                    self.right_rotate(current.parent, current, current.parent.parent)
                    w = current.parent.left

                # CASE 2
                elif w.left.color is Color.Black and w.right.color is Color.Black:
                    w.color = Color.Red
                    current = current.parent

                # CASE 3
                elif w.left.color is Color.Black:
                    w.right.color = Color.Black
                    w.color = Color.Red
                    self.left_rotate(w, w.right, w.parent)
                    w = current.parent.left

                # CASE 4
                else:
                    w.color = current.parent.color
                    current.parent.color = Color.Black
                    w.left.color = Color.Black
                    self.right_rotate(current.parent, current.parent.left, current.parent.parent)
                    if current.val is None:
                        self.root = current

        current.color = Color.Black


node_1 = Node(100)
node_1.color = Color.Black

node_2 = Node(150)
node_2.color = Color.Black
null_node_1 = Node(None)
null_node_1.color = Color.Black
node_2.left = null_node_1
null_node_1.parent = node_2

node_3 = Node(200)
null_node_2 = Node(None)
null_node_2.color = Color.Black
node_3.left = null_node_2
null_node_2.parent = node_3
null_node_3 = Node(None)
null_node_3.color = Color.Black
node_3.right = null_node_3
null_node_3.parent = node_3

node_4 = Node(75)
node_5 = Node(50)
node_5.color = Color.Black
null_node_4 = Node(None)
null_node_4.color = Color.Black
node_5.left = null_node_4
null_node_4.parent = node_5
null_node_5 = Node(None)
null_node_5.color = Color.Black
node_5.right = null_node_5
null_node_5.parent = node_5

node_6 = Node(80)
node_6.color = Color.Black
null_node_6 = Node(None)
node_6.left = null_node_6
null_node_6.color = Color.Black
null_node_6.parent = node_6

node_7 = Node(91)
null_node_7 = Node(None)
null_node_7.color = Color.Black
node_7.left = null_node_7
null_node_7.parent = node_7
null_node_8 = Node(None)
null_node_8.color = Color.Black
node_7.right = null_node_8
null_node_8.parent = node_7

tree = RBTree(node_1)

tree.root.right = node_2
node_2.parent = tree.root

tree.root.right.right = node_3
node_3.parent = tree.root.right

tree.root.left = node_4
node_4.parent = tree.root

tree.root.left.left = node_5
node_5.parent = tree.root.left

tree.root.left.right = node_6
node_6.parent = tree.root.left

tree.root.left.right.right = node_7
node_7.parent = tree.root.left.right


tree.delete_node(node_6)
print("Che")

