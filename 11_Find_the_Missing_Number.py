''' 
Finding the missing number in an array :
Given an array containing a range of numbers from 0 to n with a missing number,
find the missing number in the input array.
'''


def find_missing_numbers(nums):
    if not nums:
        return []
    
    n = max(nums)
    full_set = set(range(0, n + 1))
    return sorted(full_set - set(nums))



# Test Cases
print(find_missing_numbers([0, 1, 3, 4, 5, 6, 8, 9, 10]))  # [2, 7]
print(find_missing_numbers([0, 1, 2, 3, 4, 5, 6, 8, 9, 10]))  # [7]
print(find_missing_numbers([1, 2, 3]))   # [0]  → 0 is missing
print(find_missing_numbers([]))          # []   → empty input