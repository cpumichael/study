
import heapq

def max_candies(arr, k):
    arr = [-1*i for i in arr]
    heapq.heapify(arr)
    eaten = 0
    for i in range(k):
        chomp = -1 * arr[0]
        eaten += chomp
        heapq.heapreplace(arr, -1 * (chomp // 2))
    return eaten

print(max_candies([2,1,7,4,2], 3))

# vim: ai sw=4 ts=4 et showmatch
