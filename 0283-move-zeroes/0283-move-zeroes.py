class Solution:
    def moveZeroes(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(a) < 2 :
            return 
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i] == 0 and a[j]!=0:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
                    break
            
