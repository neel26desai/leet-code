from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #generate the frequency count of each chahracter
        char_count = Counter(s)
        #iterate throught the string and return the index of first element with the count as 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1

        


if __name__=="__main__":
    s0=Solution()
    s = "leetcode"
    print(s0.firstUniqChar(s))
    s = "loveleetcode"
    print(s0.firstUniqChar(s))
    s = "aabb"
    print(s0.firstUniqChar(s))

        