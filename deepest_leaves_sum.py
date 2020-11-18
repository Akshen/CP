# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        q = [root]
        while q:
            ll = len(q)
            result = 0
            for _ in range(ll):
                node = q.pop(0)
                result += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
