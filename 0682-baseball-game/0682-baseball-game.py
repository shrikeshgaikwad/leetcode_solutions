class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in operations:
            if i.lstrip("-").isdigit():
                record.append(int(i))

            elif i == "C":
                record.pop()

            elif i == "D":
                record.append(record[-1] * 2)

            elif i == "+":
                record.append(record[-1] + record[-2])

        return sum(record)