import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert everything to lower case
        #extract only the alpha numeric terms form the string using regular expression
        s= re.sub('[^a-z0-9]','',s.lower())#we are substitution anything that a not a alphabet or number with empty space
        return s==s[::-1] 


if __name__=="__main__":
    so=Solution()
    s = "race a car"
    print(so.isPalindrome(s))
    s = "A man, a plan, a canal: Panama"
    print(so.isPalindrome(s))
    s = " "
    print(so.isPalindrome(s))
