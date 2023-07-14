def sum13(nums):
    num_13 = nums.count(13)
    
    if num_13 > 0:
        luck_index = nums.index(13)
        nums.pop(luck_index)

        if len(nums) > luck_index:
            if nums[luck_index] != 13:
                nums.pop(luck_index)
                
            sum13(nums)

    return sum(nums)
                        
print(sum13([13, 13]))                  
print(sum13([13, 0, 13]))   
print(sum13([13, 3, 2, 13, 13, 13, 13]))
print(sum13([13, 1, 2, 13, 2, 1, 13]))
print(sum13([]))   
print(sum13([5, 7, 2]))
print(sum13([5, 13, 2]))