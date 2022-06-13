
from quicksort import *
from binarytree import *
from binarysearchtree import *

"""Test quick sort.
Input a list.
Output a sorted list."""
array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
sort = QuickSort(array)
print(sort.quicksort())


"""Test quick sort.
Input a list.
Output a sorted list."""

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())

"""Test binary search tree.
"""
# Set up tree
bst_tree = BST(4)

# Insert elements
bst_tree.insert(2)
bst_tree.insert(1)
bst_tree.insert(3)
bst_tree.insert(5)

# Check search
# Should be True
print(bst_tree.search(4))
# Should be False
print(bst_tree.search(6))
