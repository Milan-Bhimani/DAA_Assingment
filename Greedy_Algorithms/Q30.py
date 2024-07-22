def largest_permutation(k, arr):
    arr.sort(reverse=True)
    res = []
    for i in range(len(arr)):
        if k >= arr[i]:
            res.append(arr[i])
            k -= arr[i]
        else:
            res.append(k)
            break
    return res

k = 3
arr = [2, 1, 4, 6, 8, 5]
print(largest_permutation(k, arr))

k = 5
arr = [4, 4, 7, 5, 3]
print(largest_permutation(k, arr))