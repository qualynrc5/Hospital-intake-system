class DoctorNode:
    """Represents doctor in the reporting tree."""
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    """Manages binary tree of doctors."""
    def __init__(self):
        self.root = None

    def _find(self, node, name):
        """Recursively search for doctor by name."""
        if node is None:
            return None
        if node.name == name:
            return node
        left = self._find(node.left, name)
        if left:
            return left
        return self._find(node.right, name)

    def insert(self, parent_name, child_name, side):
        """Insert new doctor node under given parent on 'left' or 'right'."""
        parent = self._find(self.root, parent_name)
        if parent is None:
            print(f"Error: Parent '{parent_name}' not found in the tree.")
            return
        if side not in ["left", "right"]:
            print("Error: Side must be 'left' or 'right'.")
            return

        new_node = DoctorNode(child_name)
        if side == "left":
            if parent.left is None:
                parent.left = new_node
            else:
                print(f"Warning: {parent_name} already has a left report.")
        else:
            if parent.right is None:
                parent.right = new_node
            else:
                print(f"Warning: {parent_name} already has a right report.")

    # === Traversals ===
    def preorder(self, node):
        """Root -> Left -> Right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Left -> Root -> Right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Left -> Right -> Root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# === Test Example ===
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
