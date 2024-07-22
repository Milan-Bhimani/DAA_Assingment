def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals:
        last = merged[-1]

        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals)) 
intervals = [[1, 4], [4, 5]]
print(merge(intervals))