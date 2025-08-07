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
    

    class Solution1:
        def twoSum(self, nums, target):
            num_index = {}

            for i, number in enumerate(nums):
                num_index[number] = i

            for i, number in enumerate(nums):
                complement = target - number
                if(complement in num_index and num_index[complement] != i):
                    return [i, num_index[complement]]
                

    class Solution2:
        def maxArea(self, height: list[int]) -> int:
            l = 0
            r = len(height) -1
            max_area = float('-inf')
            
            while l < r:
                area = min(height[l], height[r]) * (r-l)
                max_area = max(max_area, area)
                
                if height[l] < height[r]:
                    l += 1
                    
                else:
                    r -= 1
                    
            return int(max_area) 
        

    class Solution3:
        def intToRoman(self, num: int) -> str:
            # using list of lists instead of a dictionary because we want the iteration to be ordered
            symbol_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],["X", 10], ["XL", 40], ["L", 50], ["XC", 90], 
                        ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
            
            result = ""
            
            for sym, val in reversed(symbol_list):
                if num // val:
                    count = num // val
                    result += (sym * count)
                    num = num % val
                    
            return result
        

    class Solution4:
        def romanToInt(self, s: str) -> int:
            symbol_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000,}
            
            result = 0
            
            for i in range(len(s)):
                if i + 1 < len(s) and symbol_map[s[i]] < symbol_map[s[i + 1]]:
                    result -= symbol_map[s[i]]
                    
                else: 
                    result += symbol_map[s[i]]
            
            return result
        

    class Solution5:
        def threeSum(self, nums: list[int]) -> list[list[int]]:
            result = []
            nums.sort()

            for i, a in enumerate(nums):
                if i > 0 and a == nums[i - 1]:
                    continue

                l, r = i + 1, len(nums) - 1
                while l < r:
                    threeSum = a + nums[l] + nums[r]
                    if threeSum > 0:
                        r -= 1
                    elif threeSum < 0: 
                        l += 1
                    else: 
                        result.append([a, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
            return result