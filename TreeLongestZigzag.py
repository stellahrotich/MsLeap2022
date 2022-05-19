# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task
def solution(T):
    res = float ('-inf')
    def dfs(node, direction, longest_zigzag):
        nonlocal res
        if (node.l is None and node.r is None):
            res = max(res, longest_zigzag)
        else:
            if (node.l is not None):
                dfs(node.l, -1, longest_zigzag - min(direction * -1, 0))

            if (node.r is not None):
                dfs(node.r, 1, longest_zigzag - min(direction * 1, 0))
                
    dfs(T, 0, 0)
    return res
