# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    state = 0
    two_count = nums.count(2)
    
    if two_count > 0: 
        for n in nums:
            if state + 1 < len(nums):
                state += 1

                if n == 2 and nums[state] == 2:                    
                    return True

    return False
print(has22([2, 2, 1, 2])) 
print(has22([5, 2, 5, 2])) 
print(has22([2, 3, 2, 2])) 