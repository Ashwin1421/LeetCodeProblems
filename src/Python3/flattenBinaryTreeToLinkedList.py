# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """

        :param root: TreeNode
        :return: void
        """
        result = []
        self.preorder(root, result)
        #result.sort()
        for i in range(len(result)-1):
            root.val = result[i]
            root.left = None
            root.right = TreeNode(result[i+1])
            root = root.right


    def preorder(self, root, orderList):
        if root:
            orderList.append(root.val)
            self.preorder(root.left, orderList)
            self.preorder(root.right, orderList)
        