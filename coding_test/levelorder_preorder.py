from collections import deque

class TreeNode:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value

def maxDepth(root):
    if root is None:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return max(left_depth, right_depth) + 1 # 오른쪽 or 왼쪽 노드의 반환값 중 큰 것애서 + 1

root = TreeNode(value=3)
root.left = TreeNode(value=9)
root.right = TreeNode(value=20)
root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)

print(maxDepth(root))
