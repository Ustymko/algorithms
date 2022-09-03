from avl_tree import *


def main():
    node_1 = Node(50)
    node_2 = Node(10)
    node_3 = Node(70)
    node_4 = Node(5)
    node_5 = Node(8)
    node_6 = Node(120)
    node_7 = Node(100)
    node_8 = Node(41)
    node_9 = Node(75)
    node_10 = Node(6)
    node_11 = Node(1)
    node_12 = Node(18)
    node_13 = Node(52)
    node_14 = Node(12)
    node_15 = Node(13)
    node_16 = Node(95)
    node_17 = Node(9)
    node_18 = Node(80)
    node_19 = Node(65)
    node_20 = Node(21)
    node_21 = Node(22)

    tree = AvlTree(node_1)
    tree.insert(node_2)
    tree.insert(node_3)
    tree.insert(node_4)
    tree.insert(node_5)
    tree.insert(node_6)
    tree.insert(node_7)
    tree.insert(node_8)
    tree.insert(node_9)
    tree.insert(node_10)
    tree.insert(node_11)
    tree.insert(node_12)
    tree.insert(node_13)
    tree.insert(node_14)
    tree.insert(node_15)
    tree.insert(node_16)
    tree.insert(node_17)
    tree.insert(node_18)
    tree.insert(node_19)
    tree.insert(node_20)
    tree.insert(node_21)
    tree.in_order_tree_output()


if __name__ == "__main__":
    main()


