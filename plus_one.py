class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        final = []
        #cause we have to add 1 initialit so setting carry as 1
        carry=1
        for i in range(len(digits)-1,-1,-1):
            total = digits[i]+carry
            if total>=10:
                carry=1
                val = total%10
                final.append(val)
            else:
                carry = 0
                final.append(total)
        if carry !=0:
            final.append(carry)
        
        return final[::-1]
                
                
        
if __name__=="__main__":
    s=Solution()
    digits=[1,2,3]
    print(s.plusOne(digits))
    digits=[9]
    print(s.plusOne(digits))