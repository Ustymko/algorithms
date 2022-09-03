from typing import Optional
from functions import *


class AvlTree:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, new_node: Node):
        if self.root:
            self.insert_node(self.root, new_node)
        else:
            self.root = new_node

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
            grandfather.max_height = 1 + max(check_max_height(grandfather.left),
                                             check_max_height(grandfather.right))
        else:
            self.root = child
        father.max_height = 1 + max(check_max_height(father.left), check_max_height(father.right))
        child.max_height = 1 + max(check_max_height(child.left), check_max_height(child.right))

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
            grandfather.max_height = 1 + max(check_max_height(grandfather.left),
                                             check_max_height(grandfather.right))
        else:
            self.root = child
        father.max_height = 1 + max(check_max_height(father.left), check_max_height(father.right))
        child.max_height = 1 + max(check_max_height(child.left), check_max_height(child.right))

    def insert_node(self, current_node: Node, new_node: Node):
        if new_node.val > current_node.val:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node
                new_node.parent = current_node
        else:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
                new_node.parent = current_node

        current_node = new_node.parent
        update_all_max_height(current_node)

        while current_node:
            temp_balance_factor = check_max_height(current_node.left) - \
                                  check_max_height(current_node.right)
            # Left-Left case
            if temp_balance_factor > 1 and new_node.val < current_node.left.val:
                if current_node.parent:
                    self.right_rotate(current_node, current_node.left, current_node.parent)
                else:
                    self.right_rotate(current_node, current_node.left, None)

            # Right-Right case
            elif temp_balance_factor < -1 and new_node.val > current_node.right.val:
                if current_node.parent:
                    self.left_rotate(current_node, current_node.right, current_node.parent)
                else:
                    self.left_rotate(current_node, current_node.right, None)

            # Right Left case
            elif temp_balance_factor < -1 and new_node.val < current_node.right.val:
                self.right_rotate(current_node.right, current_node.right.left, current_node)
                self.left_rotate(current_node, current_node.right, current_node.parent)

            # Left Right case
            elif temp_balance_factor > 1 and new_node.val > current_node.left.val:
                self.left_rotate(current_node.left, current_node.left.right, current_node)
                self.right_rotate(current_node, current_node.left, current_node.parent)
            update_all_max_height(current_node)
            current_node = current_node.parent

    def in_order_output(self, current_node: Node):
        if not current_node:
            return
        print(current_node.val)
        self.in_order_output(current_node.left)
        self.in_order_output(current_node.right)

    def in_order_tree_output(self):
        if self.root:
            self.in_order_output(self.root)
        else:
            return
