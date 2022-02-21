class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        self.nums = nums
        count = 1
        temp = 0

        for i in range(len(nums)):
            if self.nums[temp] == self.nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                temp = i
                count = 1 
        
        return self.nums[temp]





