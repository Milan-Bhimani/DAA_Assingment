def sankalp_sequence(a, b, n):
    if n % 3 == 0:
        return a
    elif n % 3 == 1:
        return b
    else:
        return a ^ b

def solve_sankalp_sequence(T, test_cases):
    results = []
    for case in test_cases:
        a, b, n = case
        result = sankalp_sequence(a, b, n)
        results.append(result)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    a, b, n = map(int, input().split())
    test_cases.append((a, b, n))

results = solve_sankalp_sequence(T, test_cases)

for result in results:
    print(result)