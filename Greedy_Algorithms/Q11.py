def maxMeetings(S, F):
    n = len(S)
    meetings = list(zip(S, F))
    meetings.sort(key=lambda x: x[1])
    ans = [1]
    end = meetings[0][1]
    for i in range(1, n):
        if meetings[i][0] >= end:
            ans.append(i + 1)
            end = meetings[i][1]
    return ans