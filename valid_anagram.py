from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #generate a char count for both s and t and check if they match
        #instead of counter you can also use a single for loop to generate the map for both 
        if len(s)==len(t):
            s_counter = Counter(s)
            t_counter = Counter(t)
            for key in s_counter.keys():
                #check if the key exists in string t
                if key in t_counter.keys():
                    #key exists in both now compare their count
                    if s_counter[key]!=t_counter[key]:
                        #the count is not same, it cannot be an anagram
                        return False
                    else:
                        print(key)
                else:
                    #key doesnt exists in the other string
                    return False

            return True
        else:
            return False
    
        


if __name__=="__main__":
    s0=Solution()
    s,t = "rat", "cat"
    print(s0.isAnagram(s,t))
    

        