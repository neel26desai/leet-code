from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums_1_d = dict(Counter(nums1))
        nums_2_d = dict(Counter(nums2))
        nums_1_keys = nums_1_d.keys()
        nums_2_keys = nums_2_d.keys()
        final_list=[]
        
        for key in nums_2_keys:
            if key in nums_1_keys:
                #key present in both, chock values in both list and chose the minimum one
                key_count_1 = nums_1_d[key] 
                key_count_2 = nums_2_d[key]
                count = key_count_1 if key_count_1<=key_count_2 else key_count_2
                final_list.extent([key]*count)
        return final_list