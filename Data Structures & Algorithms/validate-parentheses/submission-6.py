class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d ={']':'[','}':'{',')':'('}
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in '})]' :
                if len(stack) == 0:
                    return False
                if d[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False       
            
            