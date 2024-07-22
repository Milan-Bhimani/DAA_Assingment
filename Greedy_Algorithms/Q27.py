import heapq

def find_platforms(arr, dep, n):
    arr.sort()
    dep.sort()
    pq = []
    for _ in range(n):
        heapq.heappush(pq, dep[0])
    min_platforms = 1
    for i in range(n):
        if arr[i] >= pq[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, dep[i])
        min_platforms = max(min_platforms, len(pq))
    return min_platforms
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print(find_platforms(arr, dep, n))