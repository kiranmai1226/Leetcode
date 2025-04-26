class Solution:
    def isValid(self, s: str) -> bool:
        my_dict={')':'(',']':'[','}':'{'}
        stack=[]
        for char in s:
            if char in my_dict.values():
                stack.append(char)
                
            elif char in my_dict:
                if not stack or stack[-1]!=my_dict[char]:
                    return False
                stack.pop()
                    
        return not stack

        
            
        