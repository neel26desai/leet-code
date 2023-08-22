class Solution:
    def moveZeroes_simple(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using filter to find poistion of all zeros
        zero_ids=list(filter(lambda x:True if nums[x]==0 else False,range(0,len(nums))))
        #use a bubble sort like logic to push all zeros towards left
        num_zeros = len(zero_ids)
        for i in zero_ids:
            nums.remove(0)
        nums.extend([0]*num_zeros)

        def moveZeroes(self, nums: list[int]) -> None:
            j=0 
            for i in range(0,len(nums)):
                if nums[i]!=0 and nums[j]==0:
                    #swap the two
                    nums[i],nums[j] = nums[j],nums[i]
                if nums[j]!=0:
                    j=j+1
            pass

        
if __name__ == "__main__":
    s=Solution()
    nums=[0,1,0,3,12]
    s.moveZeroes(nums)
    print(nums)
    