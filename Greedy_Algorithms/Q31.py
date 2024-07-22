def min_jumps(seats):
    n = len(seats)
    MOD = 10**9 + 7

    occupied = seats.count('x')

    res = 0

    left, right = 0, n - 1

    while seats[left] == '.':
        left += 1

    while seats[right] == '.':
        right -= 1

    while left < right:
        if seats[left] == 'x':
            left += 1
        if seats[right] == 'x':
            right -= 1
        res += (right - left) % MOD
        left += 1
        right -= 1

    return res % MOD

seats = "....x..x.....x...."
print(min_jumps(seats)) 