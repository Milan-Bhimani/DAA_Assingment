def mice_holes(mice, holes):
    mice.sort()
    holes.sort()
    max_time = 0
    for i in range(len(mice)):
        time = abs(mice[i] - holes[i])
        max_time = max(max_time, time)
    return max_time

mice = [4, -4, 2]
holes = [4, 0, 5]
print(mice_holes(mice, holes))  