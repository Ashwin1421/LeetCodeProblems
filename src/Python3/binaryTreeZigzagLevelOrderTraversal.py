# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        for lvl in range(1, self.height(root)+1):
            orderList = []
            if lvl % 2 == 0:
                orientation = True
            else:
                orientation = False
            self.levelOrder(root, lvl, orderList, orientation)
            result.append(orderList)

        return result

    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

    def levelOrder(self, root, level, orderList, orientation):
        """
        :param root: TreeNode
        :return: void
        """
        if not root:
            return None
        if level == 1:
            orderList.append(root.val)
        else:
            if not orientation:
                self.levelOrder(root.left, level - 1, orderList, orientation)
                self.levelOrder(root.right, level - 1, orderList, orientation)
            else:
                self.levelOrder(root.right, level - 1, orderList, orientation)
                self.levelOrder(root.left, level - 1, orderList, orientation)