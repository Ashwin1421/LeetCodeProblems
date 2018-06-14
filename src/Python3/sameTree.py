# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        print(self.height(p))
        print(self.height(q))
        if self.height(p) != self.height(q):
            return False
        else:
            for i in range(1,self.height(p)+1):
                levelList_p = [None for x in range(int(pow(2,self.height(p))))]
                levelList_q = [None for x in range(int(pow(2,self.height(p))))]
                self.levelOrder(p, i, levelList_p, 0, int(pow(2,self.height(p))))
                self.levelOrder(q, i, levelList_q, 0, int(pow(2,self.height(q))))
                if levelList_p != levelList_q:
                    return False
        
        return True
        
    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        return max(self.height(root.left), self.height(root.right))+1
    
    def levelOrder(self, root, level, levelList, start, end):
        """
        :type root: TreeNode
        :type level: int
        :type levelList: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        if root is None:
            return
        if level == 1:
            levelList[(start+end)//2] = root.val
        else:
            mid = (start+end)//2
            self.levelOrder(root.left, level-1, levelList, start, mid-1)
            self.levelOrder(root.right, level-1, levelList, mid+1, end)