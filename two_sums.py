class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d={}
        for n,i in enumerate(nums):
            if i in d.keys():
                return [d[i],n]
            else:
                d[target-i]= n 
        print(d)

if __name__=="__main__":
    s= Solution()
    nums= [2,7,11,15]
    target=9
    print(s.twoSum(nums,target))
    