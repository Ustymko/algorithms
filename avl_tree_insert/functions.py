from node import Node


def check_max_height(current_node: Node):
    if not current_node:
        return 0
    return current_node.max_height


def update_all_max_height(current_node: Node):
    while current_node:
        current_node.max_height = 1 + max(check_max_height(current_node.left),
                                          check_max_height(current_node.right))
        current_node = current_node.parent
