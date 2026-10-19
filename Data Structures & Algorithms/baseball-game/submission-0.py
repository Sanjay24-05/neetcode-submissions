class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for cur in operations:
            if cur == 'D':
                calc= result[-1]*2
                result.append(calc)
            elif cur == 'C':
                result.pop()
            elif cur == '+':
                result.append(result[-1]+result[-2])
            else:
                result.append(int(cur))
        return sum(result)        
        