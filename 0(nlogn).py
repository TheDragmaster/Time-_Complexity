# Marginally less efficient than O(n) but much more efficient than O(n^2)
# Typically built in sorting algorithms use 0(nlogn)

#HeapSort
import heapq
nums = [1, 2, 3, 4, 5]
heapq.heapify(nums)     #O(n)
while nums:
    heapq.heappop(nums) # O(logn)

#MergeSort
