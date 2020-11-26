# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return 0
        
        X = self._height(root, x, 0)
        Y = self._height(root, y, 0)
        px = self._parent(root, x)
        py = self._parent(root, y)
        if px == py:
            return 0
        return X==Y
    
    def _height(self, node, target, count):
        if not node:
            return
        if node.val == target:
            return count

        l = self._height(node.left, target, count+1)
        r = self._height(node.right, target, count+1)
        
        if l != None:
            return l
        else:
            return r
        
    def _parent(self, node, target):
        stk = [node]
        while stk:
            nn = stk.pop()
            if nn.left:
                if nn.left.val == target:
                    return nn.val
                stk.append(nn.left)
            if nn.right:
                if nn.right.val == target:
                    return nn.val
                stk.append(nn.right)
                
