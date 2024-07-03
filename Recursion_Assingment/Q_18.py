def geek_onacci(A, B, C, N, memo):
    if N == 1:
        return A
    if N == 2:
        return B
    if N == 3:
        return C

    if N in memo:
        return memo[N]

    memo[N] = geek_onacci(A, B, C, N-1, memo) + geek_onacci(A, B, C, N-2, memo) + geek_onacci(A, B, C, N-3, memo)
    return memo[N]

def solve_geek_onacci_series(T, test_cases):
    results = []
    for case in test_cases:
        A, B, C, N = case
        memo = {}
        result = geek_onacci(A, B, C, N, memo)
        results.append(result)
    return results


T = int(input("Enter number of test cases: "))
test_cases = []
for _ in range(T):
    A, B, C, N = map(int, input("Enter A, B, C, N: ").split())
    test_cases.append((A, B, C, N))


results = solve_geek_onacci_series(T, test_cases)


for result in results:
    print(result)
