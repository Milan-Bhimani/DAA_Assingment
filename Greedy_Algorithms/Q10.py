def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    end_time = -1
    count = 0
    for start, end in meetings:
        if start > end_time:
            end_time = end
            count += 1
    return count