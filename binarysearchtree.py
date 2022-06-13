class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.bst_insert(self.root, new_val)
        pass

    def bst_insert(self, start, new_val):
        new_node = Node(new_val)
        if start.value > new_val:
            if start.left:
                self.bst_search(start.left, new_val)
            else:
                start.left = new_node
        elif start.value < new_val:
            if start.right:
                self.bst_search(start.right, new_val)
            else:
                start.right = new_node
        pass

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.bst_search(start.left, find_val)
            else:
                return self.bst_search(start.right, find_val)
        return False
