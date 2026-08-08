class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if target - a[j] == a[i]:
                    return [i,j]
        