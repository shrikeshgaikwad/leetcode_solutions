class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        positives = []
        negatives = []

        for i in a :
            if i > 0 :
                positives.append(i)
            else:
                negatives.append(i)
        j = 0
        for i in range(len(a)//2):
            a[j] = positives[i]
            a[j+1] = negatives[i]
            j+=2

        return a