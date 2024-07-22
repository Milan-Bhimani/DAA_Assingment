def catch_thieves(arr, n, k):
    policemen = []
    thieves = []
    
    for i in range(n):
        if arr[i] == 'P':
            policemen.append(i)
        else:
            thieves.append(i)
    
    policemen.sort()
    thieves.sort()
    
    i = j = 0
    caught = 0
    
    while i < len(policemen) and j < len(thieves):
        if abs(policemen[i] - thieves[j]) <= k:
            caught += 1
            i += 1
            j += 1
        else:
            if policemen[i] < thieves[j]:
                i += 1
            else:
                j += 1
    
    return caught

arr = ['P', 'T', 'P', 'T', 'T', 'P']
n = len(arr)
k = 2
print(catch_thieves(arr, n, k))