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
    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(columns) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                    



        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
    



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next
    

    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            A, B = nums1, nums2
            total = len(nums1) + len(nums2)
            half = total // 2
                
            if len(B) < len(A):
                A, B = B, A
                
            l, r = 0, len(A) - 1
            while True:
                i = (l + r) // 2
                j = half - i - 2
                
                Aleft = A[i] if i >= 0 else float("-infinity")
                Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
                
                Bleft = B[j] if j >= 0 else float("-infinity")
                Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
                
                
                if Aleft <= Bright and Bleft  <= Aright:
                    if total % 2:
                        return min(Aright, Bright)
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                elif Aleft > Bright:
                    r = i - 1
                    
                else:
                    l = i + 1





# Amazon Interview Question

def maximizeProdOps(s: str) -> int:
    if not s:
        return 0  # empty string => no ops possible

    start_char = s[0]
    end_char = s[-1]

    # Find rightmost occurrence of start_char (can't remove before this)
    left_bound = 0
    for i in range(len(s)):
        if s[i] == start_char:
            left_bound = i

    # Find leftmost occurrence of end_char (can't remove after this)
    right_bound = len(s) - 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == end_char:
            right_bound = i

    # Minimal preserved segment
    if left_bound > right_bound:
        # No valid segment found — means string already fails to match type
        return 0

    preserved_length = right_bound - left_bound + 1
    max_operations = len(s) - preserved_length

    return max_operations


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}

        for i in nums:
            if i in duplicate:
                return True
            duplicate[i] = True
        return False



class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n**(1/3) != 3:
            return False
        return True
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        resultMap = {}  # key: sorted letters or letter counts, value: list of anagrams
        
        for word in strs:
            # Sort the characters to make the key
            key = tuple(sorted(word))
            
            # Add to dictionary
            if key not in resultMap:
                resultMap[key] = []
            resultMap[key].append(word)
        
        return list(resultMap.values())