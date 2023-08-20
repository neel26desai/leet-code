class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        #python allows for such kind of swap
        if k>0:
            nums[:k],nums[k:] = nums[-k:],nums[:-k]

if __name__=="__main__":
    s=Solution()
    nums=[1,2,3,4,5,6,7]
    s.rotate(nums,3)
    print(nums)