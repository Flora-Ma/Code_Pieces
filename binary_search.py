# nums should be in ascending order
def binary_search(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= k: # Update to your condition
            r = mid
        else:
            l = mid + 1
    return l if nums[l] == k else -1 # Update to your own return behavior

# In this template, l == r == mid in the final and there won't be infinite loop(l or r will be updated).
# Remember this when customizing your own behavior.

def binary_search_last_appearance(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == k and nums[mid + 1] > k: 
            return mid
        elif nums[mid] > k:
            r = mid
        else:
            l = mid + 1
    return l if nums[l] == k else -1

def binary_search_last_appearance_2(nums, k):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= k and nums[mid + 1] > k: 
            r = mid
        else:
            l = mid + 1
    return l if nums[l] == k else -1

print(binary_search([1, 4, 5, 9], 9))
print(binary_search([1, 4, 5, 9], 1))
print(binary_search([1, 4, 5, 9], 3))
print(binary_search([1, 4, 4, 4, 9], 4)) # first appearance
print(binary_search_last_appearance([1, 4, 4, 4, 9], 4))
print(binary_search_last_appearance_2([1, 4, 4, 4, 9], 4))

# python has libraray functions for binary search.
import bisect # this module provides support for maintaining a list in sorted order without having to sort the list after each insertion.
a = [1, 4, 4, 5, 9]
i = bisect.bisect_left(a, 4) # Locate the insertion point for x=4 in a to maintain sorted order. If x is already present in a, the insertion point will be before(to the left of) any existing entries.
print(f'bisect_left={i}')
i = bisect.bisect_right(a, 4)
print(f'bisect_right={i}')
i = bisect.bisect(a, 4) # Same with bisect_right
print(f'bisect={i}')
