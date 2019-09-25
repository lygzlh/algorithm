# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.list=[]
    def inorderTraversal(self, root):
        """
        list保存输出
        先序遍历：左孩子节点->根节点->右孩子节点
        根据顺序来使用递归
        :type root: TreeNode
        :rtype: List[int]
        """
        if root!=None:
            if root.left:
                self.inorderTraversal(root.left)
            self.list.append(root.val)
            if root.right:
                self.inorderTraversal(root.right)
        return self.list