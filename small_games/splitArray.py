import time


def split_array(nums):
    nums.sort(reverse=True)
    group1 = []
    group2 = []

    sum_group1 = 0
    sum_group2 = sum(nums) / 2

    num_counts = {}
    for num in nums:
        num_counts[num] = num_counts.get(num, 0) + 1

    for num in nums:
        diff = sum_group2 - sum_group1
        count_duplicates = num_counts[num]
        sum_of_duplicates = count_duplicates * num
        gap_diff_and_sum_of_duplicates = diff - sum_of_duplicates

        if num in group1 or (diff >= 0 and count_duplicates == 1) or gap_diff_and_sum_of_duplicates > 0 or diff >= 0.5 * sum_of_duplicates:
            group1.append(num)
            sum_group1 += num
        else:
            group2.append(num)

    return group1, group2

nums = [1, 1, 1, 3, 3, 3, 3, 3, 3, 2, 3, 3, 2, 2, 1]
start = time.time()
group1, group2 = split_array(nums)
end = time.time()

print("Group 1:", group1)
print("Group 2:", group2)
print("Execution time: ", end - start)
