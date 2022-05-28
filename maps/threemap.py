import unittest


class Threemap:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#обход дерева
def inorder(root):
    if root is not None:
        # обходим влево
        inorder(root.left)

        # Обходим корень
        print(str(root.key) + " -", end=' ')

        # обходим вправо
        inorder(root.right)

#вставка
def insert(node, key):
    if node is None:
        return Threemap(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def minValueNode(node):
    current = node
    # ищем крайний левый лист
    while(current.left is not None):
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root

class MapTestMixin:
    root = None
    root = insert(root, 5)
    root = insert(root, 2)
    root = insert(root, 1)
    root = insert(root, 9)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 25)
    root = insert(root, 11)
    root = insert(root, 6)
    print("Отсортированный обход: ", end=' ')
    inorder(root)

    print("\nПосле удаления 11")
    root = deleteNode(root, 11)

    print("Отсортированный обход: ", end=' ')
    inorder(root)

class TreeMapTest(MapTestMixin, unittest.TestCase):
    map_cls = dict


unittest.main(argv=[''], verbosity=2, exit=False)