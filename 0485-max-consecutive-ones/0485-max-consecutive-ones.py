class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        num = 0 
        maxNum = 0 

        for i in range(len(a)):
            if a[i] != 1:
                num = 0 
                continue
            else:
                num+=1 
                if num > maxNum :
                    maxNum = num 

        return maxNum 