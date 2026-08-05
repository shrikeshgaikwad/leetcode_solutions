class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        for i in range(len(positives)):
            nums[2 * i] = positives[i]
            nums[2 * i + 1] = negatives[i]

        return nums