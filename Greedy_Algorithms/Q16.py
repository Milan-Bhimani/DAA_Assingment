import heapq

def min_cost_to_connect_ropes(arr):
    heap = []
    for rope in arr:
        heapq.heappush(heap, rope)
    total_cost = 0
    while len(heap) > 1:
        rope1 = heapq.heappop(heap)
        rope2 = heapq.heappop(heap)
        cost = rope1 + rope2
        total_cost += cost
        heapq.heappush(heap, cost)

    return total_cost