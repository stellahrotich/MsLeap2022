# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Tree  # library with types used in the task

def solution(T):
    # write your code in Python 3.6
    return get_path(T, 0, 0)


def get_path(T, leftPath, rightPath):
    max_path = max(leftPath, rightPath)  # 0, 0 [1]
    if T.l:
        max_path = max(max_path, get_path(T.l, leftPath + 1, 0))  # 1 , 2
        # l = 1 + solution(T.l)
        # get the maximum for the left
    if T.r:
        max_path = max(max_path, get_path(T.r, 0, rightPath + 1))  # 1, 1

    return max_path
