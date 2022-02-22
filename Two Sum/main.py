#from typing import List

class Solution: 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, value in enumerate(nums):
            if target - value in my_dict:
                return [my_dict[target - value], index]
            else:
                my_dict[value] = index   
             



#print(Solution().twoSum([3,3],6))        


