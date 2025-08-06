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
                

    class Solution:
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
        

    class Solution:
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