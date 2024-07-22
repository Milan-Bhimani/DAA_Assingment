def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    dp = [0] * (max_deadline + 1)

    for job in jobs:
        job_id, deadline, profit = job
        for i in range(deadline, 0, -1):
            dp[i] = max(dp[i], dp[i-1])
            dp[i] = max(dp[i], dp[i-deadline] + profit)

    max_profit = dp[max_deadline]
    job_count = 0
    i = max_deadline
    while i > 0:
        if dp[i] != dp[i-1]:
            job_count += 1
            i -= deadline
        else:
            i -= 1

    return job_count, max_profit