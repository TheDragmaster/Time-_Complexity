# Binary search is (logn)       Basically keep cutting in half until you get to your solutions
nums = [1, 2, 3, 4, 5]
target = 6
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        print(m)
        break

# Binary search on Binary Search Tree is also (logn)    Cut the tree in half and only go one direction
def search(root, target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    else:
        return True
    
#Heap Push and Pop is also (logn)
import heapq
minHeap = []
heapq.heappush(minHeap, 5)
heapq.heappop(minHeap)
