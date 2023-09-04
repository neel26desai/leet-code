import re
class Solution:
    def myAtoi(self,s: str) -> int:
        # Define constants for 32-bit signed integer maximum and minimum values
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Remove leading whitespaces
        s = s.lstrip()
        
        # Check if string is empty after removing whitespaces
        if not s:
            return 0
        
        # Determine the sign
        sign = -1 if s[0] == '-' else 1
        
        # If there's a sign character, remove it
        if s[0] in ['+', '-']:
            s = s[1:]
        
        # Convert string to integer
        i, n = 0, len(s)
        while i < n and s[i].isdigit():
            i += 1
        num = int(s[:i]) if i > 0 else 0
        
        # Apply the sign
        num *= sign
        
        # Handle overflow and underflow
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        
        return num

if __name__=="__main__":
    so=Solution()
    s = "42"
    print(so.myAtoi(s))
    s = "   -42"
    print(so.myAtoi(s))
    s = "4193 with words"
    print(so.myAtoi(s))