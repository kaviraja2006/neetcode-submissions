class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashmap={
            ']':'[', 
            '}':'{',
            ')':'('
        }
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack or stack[-1]!=hashmap[i]:
                    return False
                stack.pop()
        return not stack                
        