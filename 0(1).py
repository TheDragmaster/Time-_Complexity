# 0(1) time complexity will always take the same amount of time to edxectue no matter what the input is

# Array
nums = [1, 2, 3]  # push value to end is 0(1)
nums.append(4)  # pop value from end is  0(1)
nums[0]  # Looking up a value is just 0(1)
nums[1]
nums[2]


#HashMap / Set
hashmap = {}
hashmap["key"] = 10  # Insert is 0(1)
print("key" in hashmap)  # lookup is 0(1)
print(hashmap["key"])
hashmap.pop("key")  # Remove is 0(1)
