class Solution:
    def lengthOfLongestSubstring_old(self, s: str) -> int:
        sub_string =''
        max_length =0
        if len(s)>1:
            for i in s:
                if i not in sub_string:
                    #if a character is not is substring, add
                    sub_string = sub_string + i
                else:
                    #if a character is already in the substring, save the substring without the character
                    if len(sub_string)>=max_length:
                        max_length = len(sub_string)
                    sub_string = i
                    #
            #in case the last element went in if an not else 
            if len(sub_string)>=max_length:
                    max_length = len(sub_string)
            return max_length
        elif len(s)==1:
            return 1
        else:
            return 0

    def lengthOfLongestSubstring(self, s: str) -> int:
        #using set and set length,
        set_s=set()
        #max length will keep track of longest substring length
        max_length = 0
        old_length=0
        for i in s:
            set_s.add(i)
            new_length = len(set_s)
            #if the old length and the new length are same that means characters are repeting
            if new_length == old_length:
                #see if the length is greater than max_length
                if new_length>=max_length:
                    max_length=new_length
                    #reset the set and add the current element
                    set_s = set(s)
                    set_s.add(i)
                    new_length=1   
            else:
                max_length=+1
            old_length = new_length

        return max_length
            


if __name__ == "__main__":
    so=Solution()
    #test case 1: abcabcbb, answer 3
    print(so.lengthOfLongestSubstring('abcabcbb'))
    #test case 2: bbbbb , answer 1
    print(so.lengthOfLongestSubstring('bbbbb'))
    #test case 3: pwwkew, answer 3
    print(so.lengthOfLongestSubstring('pwwkew'))
    #test case 3: abcw, answer 4
    print(so.lengthOfLongestSubstring('abcw'))
