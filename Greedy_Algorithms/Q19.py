import heapq

def find_platforms(arr, dep):
    arr.sort()
    dep.sort()
    platforms = 1
    curr_platforms = 1
    pq = [dep[0]]
    i = 1
    j = 1
    while i < len(arr) and j < len(dep):
        if arr[i] <= pq[0]:
            i += 1
            curr_platforms += 1
            heapq.heappush(pq, dep[i - 1])
        else:
            heapq.heappop(pq)
            curr_platforms -= 1
            j += 1
        platforms = max(platforms, curr_platforms)
    return platforms