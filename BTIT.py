'''
Binary Tree Inorder Traversal using Stacks
        1
    2       3
4     5      6   7
expected = [4, 2, 5,1,6,3,7]
'''

def inorderT(root):
    stk = []
    res = []
    while root is not None and stk != []:
        while root is not None:
            stk.append(root)
            root = root.left
        root = stk.pop()
        res.append(root.val)
        root = root.right
    return res
