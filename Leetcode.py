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
        
    class Solution6:
        def threeSumClosest(self, nums: list[int], target: int) -> int:
            nums.sort()
            closest = float('inf')
            
            for i in range(len(nums)):
                if i < 0 and nums[i] == nums[i - 1]:
                    continue
                    
                l, r = i + 1, (len(nums) - 1)
                
                while l < r:
                    curr_sum = nums[i] + nums[l] + nums[r]
                    if abs(curr_sum - target) < abs(closest - target):
                        closest = curr_sum
                    
                    if curr_sum == target:
                        return curr_sum
                    elif curr_sum < target:
                        l += 1
                    else:
                        r -= 1
            return int(closest)
        
    class Solution7:
        def strStr(self, haystack: str, needle: str) -> int:
            if needle == "":
                return 0

            for i in range(len(haystack) + 1 - len(needle)):
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
            return -1

# LinkedList Problems

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            
        return dummy.next