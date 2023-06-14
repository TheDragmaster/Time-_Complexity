#0(n) (Or linear time algorithm) Means that the time complexity will increase proportionally to the input values plugged in 

nums = [1,2,3]
sum(nums)       #sum of the array more imput = more time to solve
for n in nums:  #Looping through all the elements is also linear time complexity
    print(n)

nums. insert(1,100) #Inserting into an array is linear time algorithm
nums.remove(100)    #Removing from the middle of an array is linear time algorithm
print(100 in nums)  #Searching is a linear time algorithm 

import heapq
heapq.heapify(nums)     #Building a heap is big o(n) time

# Nested loops can sometimes be 0(n)
#(monotonic stack or sliding window)