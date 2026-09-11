class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = (s1 + " " + s2).split()

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        ans = []

        for word in freq:
            if freq[word] == 1:
                ans.append(word)

        return ans