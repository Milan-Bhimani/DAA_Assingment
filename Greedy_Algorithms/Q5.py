def average_waiting_time(bt):
    n = len(bt)
    bt.sort()
    waiting_time = 0
    total_waiting_time = 0
    for i in range(n):
        total_waiting_time += waiting_time
        waiting_time += bt[i]
    return total_waiting_time // n