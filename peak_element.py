import math

# [1, 2, 3, 1] -> 3
# l = 0, r = 3 -> m = 1, target = 2
# target > bigger than left: l = m + 1 = 2
# l = 2, r = 3 -> m = 2, target = 3
# return target

#O(N)
# O(log(N)) <---

# binary search
# divide and conquer

# [1, 4, 3, 1, 2] -> idx 1
# [..., increasing array, peak, decreasing array, ...]
# target:
# left < target  and target > right: return target (idx)
# left < target: -> increasing part
# move to the right
# target > right: -> decreasing part
# move to the left

#
def one_pass():
    left = -math.inf

    for i, n in enumerate(nums):
        if n > left and (i >= len(nums) or n > nums[i+1]):
            return i
        left = n

    return None
nums = [1,0,1,1,4,5]
# (1+4)//2 = 2
def b_search(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        print(l,r)
        m = (l+r)//2
        target = nums[m]
        bigger_than_left = m-1 < 0 or target > nums[m-1]
        bigger_than_right = (m+1 >= len(nums)) or target > nums[m+1]
        if bigger_than_left and bigger_than_right:
            return m, target
        elif bigger_than_left:
            l = m
        else:
            r = m


print(b_search(nums))