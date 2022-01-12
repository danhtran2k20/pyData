# Ion Flux Relabeling
# ===================

# Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

# Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

#    7
#  3   6
# 1 2 4 5

# Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.  For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

# The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

# =================================================

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution(5, {19, 14, 28})
# Output:
#     21,15,29

# Input:
# Solution.solution(3, {7, 3, 5, 1})
# Output:
#     -1,7,6,3

# -- Python cases --
# Input:
# solution.solution(3, [7, 3, 5, 1])
# Output:
#     -1,7,6,3

# Input:
# solution.solution(5, [19, 14, 28])
# Output:
#     21,15,29

# ==============================================


# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
class Node:
    def __init__(self, root=None):
        self.left = None
        self.right = None
        self.root = root

    # ko cần thiết
    # def __str__(self):
    #     return str(self.root)


def postorder(height, nums):
    if height == 1:
        return Node(nums.pop())
    node = Node()
    node.root = nums.pop()
    node.right = postorder(height - 1, nums)
    node.left = postorder(height - 1, nums)
    return node


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)
        # then recur on right child
        printPostorder(root.right)
        # now print the data of node
        print(root.root),


def print_preorder(root):
    if root:
        print(root.root)
        print_preorder(root.left)
        print_preorder(root.right)


# ============================================
# Ref only
# https://stackoverflow.com/questions/48875318/building-a-perfect-binary-tree-with-height-30
#
# def build_tree(h):
#     node = Node(0)
#     if h == 1:
#         return node
#     node.left = build_tree(h-1)
#     node.right = build_tree(h-1)
#     return node

# trees = Node(1)
# trees.left = Node(2)
# trees.right = Node(3)
# trees.left.left = Node(4)
# trees.left.right = Node(5)
# printPostorder(trees)

# printPostorder(build_tree(1))
# ==============================================

# https://stackoverflow.com/questions/62960591/creating-perfect-binary-trees-with-postorder-traversal


height = 5
tree = postorder(height, list(range(1, 2 ** height)))
# printPostorder(tree.right.left)
printPostorder(tree)

print(tree.left.root)


# ===================================
def solution(h, q):
    tree = postorder(h, list(range(1, 2 ** h)))
    return [search(val, tree) for val in q]


def search(val, tree, root=-1):
    if val >= tree.root:
        return root
    root = tree.root
    return (
        search(val, tree.left, root)
        if val <= tree.left.root
        else search(val, tree.right, root)
    )


print("sol 1:", solution(5, [19, 14, 28]))
print("sol 2:", solution(3, [7, 3, 5, 1]))


# ===================================
# sol2
def solution2(height, arr):
    return [search2(ele, height, 2 ** height - 1) for ele in arr]


def search2(ele, height, tree_root, root_node=-1):
    if ele >= tree_root:
        return root_node
    height = height - 1
    root_node = tree_root
    return (
        search2(ele, height, tree_root - 2 ** height, root_node)
        if ele <= tree_root - 2 ** height
        else search2(ele, height, tree_root - 1, root_node)
    )


print("sol 1:", solution2(5, [19, 14, 28]))
print("sol 2:", solution2(3, [7, 3, 5, 1]))
