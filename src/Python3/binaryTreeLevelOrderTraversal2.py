# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
    
        result = []
        for lvl in range(self.height(root),0,-1):
            orderList = []
            self.levelOrder(root, lvl, orderList)
            result.append(orderList)

        return result

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

    def levelOrder(self, root, level, orderList):
        """
        :param root: TreeNode
        :return: void
        """
        if not root:
            return None
        if level == 1:
            orderList.append(root.val)
        else:
            #if not orientation:
            self.levelOrder(root.left, level - 1, orderList)
            self.levelOrder(root.right, level - 1, orderList)