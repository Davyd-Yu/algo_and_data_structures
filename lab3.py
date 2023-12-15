from typing import List

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

def pre_order_traversal(root: BinaryTree) -> List[int]:
    result = []

    def traverse(node):
        if node:
            result.append(node.value)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return result

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

# Викликаємо функцію та виводимо результат
result = pre_order_traversal(root)
print(result)