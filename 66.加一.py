#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for index in range(len(digits)):
            sum = sum+digits[len(digits)-1-index]*(10**index)
        sum = sum+1
        result = []
        for i in str(sum):
            result.append(int(i))
        return result
        
# @lc code=end

#ideal
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]


