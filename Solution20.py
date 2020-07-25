class Solution20:
    def isValid(self, s: str) -> bool:
        stack = ['#']
        for temp in s:
            if temp == ')':
                if stack.pop() != '(':
                    return False
            elif  temp == ']':
               if stack.pop() != '[':
                    return False                      
            elif  temp == '}':
               if stack.pop() != '{':
                    return False                       
            else :
                stack.append(temp)
        if stack.pop() != '#':
            return False
        return True
