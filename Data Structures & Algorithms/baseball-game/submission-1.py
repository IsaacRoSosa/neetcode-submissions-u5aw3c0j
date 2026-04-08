class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for operation in operations:
            if operation == "+":
                record.append((int(record[-1]) + int(record[-2])))
            elif operation == "D":
                record.append(2 * int(record[-1]))
            elif operation == "C":
                record.pop()
            else:
                record.append(int(operation))

        return sum(record)      
        
    