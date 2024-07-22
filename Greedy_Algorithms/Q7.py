def distribute_chocolates(A, M):
    A.sort()
    min_diff = float('inf')
    for i in range(len(A) - M + 1):
        diff = A[i + M - 1] - A[i]
        min_diff = min(min_diff, diff)
    return min_diff