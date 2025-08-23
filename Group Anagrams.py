def groupAnagrams(strs):
    """
    Group anagrams together.
    
    Args:
        strs: List of strings
    
    Returns:
        List of lists, where each inner list contains anagrams
    """
    if not strs:
        return []
    
    resultMap = {}  # key: sorted letters, value: list of anagrams
    
    for word in strs:
        # Sort the characters to make the key
        key = tuple(sorted(word))

        
        # Add to dictionary
        if key not in resultMap:
            resultMap[key] = []
        resultMap[key].append(word)
    
    return list(resultMap.values())


# Test cases
def test_group_anagrams():
    print("Testing Group Anagrams Function")
    print("=" * 40)
    
    # Test Case 1: Basic example
    test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = groupAnagrams(test1)
    print(f"Input: {test1}")
    print(f"Output: {result1}")
    print()
    
    # Test Case 2: Empty list
    test2 = []
    result2 = groupAnagrams(test2)
    print(f"Input: {test2}")
    print(f"Output: {result2}")
    print()
    
    # Test Case 3: Single word
    test3 = ["a"]
    result3 = groupAnagrams(test3)
    print(f"Input: {test3}")
    print(f"Output: {result3}")
    print()
    
    # Test Case 4: No anagrams
    test4 = ["abc", "def", "ghi"]
    result4 = groupAnagrams(test4)
    print(f"Input: {test4}")
    print(f"Output: {result4}")
    print()
    
    # Test Case 5: All anagrams
    test5 = ["abc", "bca", "cab", "acb"]
    result5 = groupAnagrams(test5)
    print(f"Input: {test5}")
    print(f"Output: {result5}")
    print()
    
    # Test Case 6: Mixed case (if you want to handle)
    test6 = ["listen", "silent", "hello", "world"]
    result6 = groupAnagrams(test6)
    print(f"Input: {test6}")
    print(f"Output: {result6}")
    print()
    
    # Test Case 7: Empty strings and duplicates
    test7 = ["", "", "a", "aa", "aaa"]
    result7 = groupAnagrams(test7)
    print(f"Input: {test7}")
    print(f"Output: {result7}")
    print()


# Alternative implementation using Counter (more robust)
from collections import Counter

def groupAnagramsCounter(strs):
    """
    Alternative implementation using Counter for character frequency
    """
    if not strs:
        return []
    
    resultMap = {}
    
    for word in strs:
        # Count character frequencies and convert to tuple for hashing
        key = tuple(sorted(Counter(word).items()))
        
        if key not in resultMap:
            resultMap[key] = []
        resultMap[key].append(word)
    
    return list(resultMap.values())


# Run the tests
if __name__ == "__main__":
    test_group_anagrams()
    
    print("\n" + "=" * 50)
    print("Testing Counter-based implementation:")
    print("=" * 50)
    
    # Quick comparison test
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    result_sorted = groupAnagrams(test_input)
    result_counter = groupAnagramsCounter(test_input)
    
    print(f"Input: {test_input}")
    print(f"Sorted method: {result_sorted}")
    print(f"Counter method: {result_counter}")
    
    # Verify both methods give same results (order might differ)
    def normalize_result(result):
        return sorted([sorted(group) for group in result])
    
    if normalize_result(result_sorted) == normalize_result(result_counter):
        print("✅ Both methods produce equivalent results!")
    else:
        print("❌ Methods produce different results!")





 class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        l = r = 0

        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            result += 1

        return result