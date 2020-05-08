# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findParent(self, root, element, parent):
        if root == None:
            return 0
        elif root.val == element:
            return parent
        else:
            lParent = self.findParent(root.left, element, root.val)
            rParent = self.findParent(root.right, element, root.val)
            return lParent + rParent

    def getLevelUtil(self, node, data, level):
        if (node == None):
            return 0

        if (node.val == data):
            return level

        downlevel = self.getLevelUtil(node.left,
                                      data, level + 1)
        if (downlevel != 0):
            return downlevel

        downlevel = self.getLevelUtil(node.right,
                                      data, level + 1)
        return downlevel

    def getLevel(self, node, data):

        return self.getLevelUtil(node, data, 1)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

        if self.findParent(root, y, 0) != self.findParent(root, x, 0):
            if self.getLevel(root, y) == self.getLevel(root, x):
                return True

