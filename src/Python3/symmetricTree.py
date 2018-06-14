# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        result = True
        palindromeList = lambda lst: lst == lst[::-1]
        for lvl in range(1, self.height(root)+1):
            lst = []
            self.levelOrder(root, lst, lvl)
            print(lst)
            if not palindromeList(lst):
                result = False
        
        
        return result
    
    def height(self, root):
        if not root:
            return 0
        
        return max(self.height(root.left), self.height(root.right))+1
    
    def levelOrder(self, root, lst, level):
        if not root:
            lst.append(None)
        if level == 1:
            if root:
                lst.append(root.val)
            else:
                lst.append(None)
        else:
            if root.left:
                self.levelOrder(root.left, lst, level-1)
            else:
                lst.append(None)
            if root.right:
                self.levelOrder(root.right, lst, level-1)
            else:
                lst.append(None)
            