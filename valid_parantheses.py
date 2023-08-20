class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0            


if __name__=="__main__":
    so=Solution()
    #test case 1
    s = "()"
    print(so.isValid(s))
    #test case 2
    s = "()[]{}"
    print(so.isValid(s))
    #test case 3
    s = "(]"
    print(so.isValid(s))
    