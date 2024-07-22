def max_sum_elements(arr, k):
    arr.sort(reverse=True)
    return sum(arr[:k])