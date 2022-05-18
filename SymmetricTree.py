#iterative
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue1 = deque([])
        queue2 = deque([])
        queue1.append(root)
        queue2.append(root)
        while queue1 and queue2:  
            t1 = queue1.pop()
            t2 = queue2.pop()
            if ( t1 == None and t2 == None): 
                continue   
            if ( t1 == None or t2 == None): 
                return False
            if ( t1.val != t2.val): 
                return False
            queue1.append(t1.left)
            queue2.append(t2.right)
            queue1.append(t1.right)
            queue2.append(t2.left)  
        return True
