#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        count_a = 0
        count_b = 1
        for a in nums[0:n]:
            count_b = count_a+1
            for b in nums[count_b:n]:
                sum = a+b
                if(sum == target):
                    return [count_a,count_b]
                else:
                    count_b = count_b+1
            count_a = count_a+1

            
        
# @lc code=end

