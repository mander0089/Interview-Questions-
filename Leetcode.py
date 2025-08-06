class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        
        sign = 1
        result = 0
        
        if not s:
            return 0
        
        
        if s[0] == '-':
            sign = -1
        s = s[1:]
            
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            
        result = result * sign
        
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        
        return result
    

    class Solution:
        def twoSum(self, nums, target):
            num_index = {}

            for i, number in enumerate(nums):
                num_index[number] = i

            for i, number in enumerate(nums):
                complement = target - number
                if(complement in num_index and num_index[complement] != i):
                    return [i, num_index[complement]]