# from collections import deque

# def bfs(root):
#     visited = []
#     if root is None:
#         return []
    
#     q = deque()
#     q.append(root)

#     while q:
#         cur_node = q.popleft()
#         visited.append(cur_node.value)
        
#         if cur_node.left:
#             q.append(cur_node.left)
#         if cur_node.right:
#             q.append(cur_node.right)
#     return visited

from collections import deque

def maxDepth(root):
    max_depth = 0
    if root is None:
        return max_depth
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        max_depth = cur_depth
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))

root = [3, 9, 20, None, None, 15, 7]

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root))