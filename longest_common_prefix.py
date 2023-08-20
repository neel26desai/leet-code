class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        #longest common prefix, from a list of strings
        #the first word in the list will be pur reference we will compare it will all other words in the list
        #sort the list based on string length
        sorted_strs = sorted(strs, key=len)
        refernce_word = sorted_strs[0]
        number_of_words=len(strs)
        common_prefix = ""
        for j,reference_letter in enumerate(refernce_word,0):
            letter_present_in = 0
            for word in sorted_strs[1:]:
                if reference_letter==word[j]:
                    letter_present_in=letter_present_in+1
                else:
                    break
            if letter_present_in == number_of_words -1:
                common_prefix +=reference_letter
            else:
                break
        
        return common_prefix

if __name__ == "__main__":
    so=Solution()
    strs = ["flower","flow","flight"]
    print(so.longestCommonPrefix(strs))