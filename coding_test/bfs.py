# bfs : 너비 우선 탐색
from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root) # 초기세팅
    while q:
        cur_node = q.popleft()
        visited.append(cur_node.value)

        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
    return visited

bfs(root)

