# Get every triplet of elements in array 
nums = [1,2, 3]
for i in range(len(nums)):  #Three nested loops 
    for j in range(i + 1, len(nums)):
        for k in range(j + 1, len(nums)):
            print(nums[i], nums[j], nums[k])