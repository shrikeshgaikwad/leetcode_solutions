class Solution:
    def maxDepth(self, a: str) -> int:
        maxDepth = 0
        depth = 0 

        for i in a:
            if i == "(":
                depth += 1
                if depth > maxDepth :
                    maxDepth = depth
            elif i == ")":
                depth -= 1
        return maxDepth