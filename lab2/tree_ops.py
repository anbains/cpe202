import unittest

# * Section 2 (Trees)

# * dd: NumTree Data Definition

# a NumTree is one of
# - "empty", or
# - TreeNode(left, right)

class TreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def __eq__(self, other):
        return (type(other) == TreeNode
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right)
    def __repr__(self):
        return ("%r, %r, %r" % (self.value, self.left, self.right))

# * 1:

# NumTree -> int
# Returns number of elements in given tree

def size(numTree):
    if numTree == "mt":
        return 0
    return 1 + size(numTree.left) + size(numTree.right)

# * 2:

# NumTree -> int
# Returns number of nodes with empty subtrees from given tree

def num_leaves(numTree):
    if numTree == "mt":
        return 0
    if numTree.left == "mt" and numTree.right == "mt":
        return 1
    return num_leaves(numTree.left) + num_leaves(numTree.right)

# * 3:

# NumTree -> int
# Returns sum of values in the given tree

def sum(numTree):
    if numTree == "mt":
        return 0
    return numTree.value + sum(numTree.left) + sum(numTree.right)

# * 4:

# NumTree -> int
# Returns height of the given tree

# This function defaults to returning 0 because it is not implemented as per
# lab guidelines.

def height(numTree):
    return 0

# * 5:

# NumTree -> Boolean
# Returns true when a tree node with value n contains a child node with value
# 3n

def has_triple(numTree):
    if numTree == "mt":
        return False
    if ((numTree.left != "mt" 
        and numTree.value == numTree.left.value / 3) 
        or (numTree.right != "mt" 
        and numTree.value == numTree.right.value / 3)):
        return True
    return has_triple(numTree.left) or has_triple(numTree.right)

# * 6:

# NumTree -> NumTree
# Returns new tree where each value of given tree is smaller by one

def sub_one_map(numTree):
    if numTree == "mt":
        return numTree
    return (TreeNode(numTree.value - 1, sub_one_map(numTree.left), 
        sub_one_map(numTree.right)))

# * Tests : the test case class for the tree functions

class TestCase(unittest.TestCase):

    # repr tests
    def test_repr(self):
        numTree = TreeNode(4, 
                TreeNode(5, "mt", 'mt'), "mt")
        self.assertEqual(repr(numTree), "4, 5, 'mt', 'mt', 'mt'")

    # size tests
    def test_size(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        numTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(2, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        self.assertEqual(size(numTreeRoot), 1)
        self.assertEqual(size(numTree), 7)

    # num_leaves tests
    def test_num_leaves(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        numTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(2, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        self.assertEqual(num_leaves(numTreeRoot), 1)
        self.assertEqual(num_leaves(numTree), 3)

    # sum tests
    def test_sum(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        numTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(2, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        self.assertEqual(sum(numTreeRoot), 4)
        self.assertEqual(sum(numTree), 186)

    # height tests
    def test_height(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        self.assertEqual(height(numTreeRoot), 0)


    # has_triple tests
    def test_has_triple(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        numTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(27, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        noTripleTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(2, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        self.assertFalse(has_triple(numTreeRoot))
        self.assertFalse(has_triple(noTripleTree))
        self.assertTrue(has_triple(numTree))

    # sub_one_map tests
    def test_sub_one_map(self):
        numTreeRoot = TreeNode(4, "mt", "mt")
        subNumTreeRoot = TreeNode(3, "mt", "mt")
        numTree = TreeNode(4,
                    TreeNode(9,
                        TreeNode(19, "mt", "mt"),
                        TreeNode(2, TreeNode(103, "mt", "mt"), "mt")
                    ),
                    TreeNode(42, "mt", TreeNode(7, "mt", "mt"))
                  )
        subNumTree = TreeNode(3,
                    TreeNode(8,
                        TreeNode(18, "mt", "mt"),
                        TreeNode(1, TreeNode(102, "mt", "mt"), "mt")
                    ),
                    TreeNode(41, "mt", TreeNode(6, "mt", "mt"))
                  )
        self.assertEqual(sub_one_map(numTreeRoot), subNumTreeRoot)
        self.assertEqual(sub_one_map(numTree), subNumTree)


if (__name__ == '__main__'):
    unittest.main()
