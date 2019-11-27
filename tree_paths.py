
# Given a binary tree, return all paths from the root to leaves.

# For example, given the tree:

#    1
#   / \
#  2   3
#     / \
#    4   5
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].



class Node(object):

    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


tree = Node(1, left = Node(2), right=Node(3, left=Node(4), right=Node(5)))


def print_dirs(tree):

    def _helper(cur_node, prev_vals):

        if not cur_node.left and not cur_node.right:
            new_ls = prev_vals[:]
            new_ls.append(cur_node.value)
            return [new_ls]

        new_vals = prev_vals + [cur_node.value]
        left_lists, right_lists = [], []

        if cur_node.left:
            left_lists = _helper(cur_node.left, new_vals)

        if cur_node.right:
            right_lists = _helper(cur_node.right, new_vals)

        return right_lists + left_lists 
    return _helper(tree, [])

assert print_dirs(tree) == [[1, 3, 5], [1, 3, 4], [1, 2]]

