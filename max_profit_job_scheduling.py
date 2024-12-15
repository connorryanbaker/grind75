def job_scheduling(start_time: List[int], end_time: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(start_time, end_time, profit))
    dp = [-1] * len(jobs)
    dp[-1] = jobs[-1][2]
    for idx in reversed(range(len(jobs) - 1)):
        next_idx = None
        l, r = idx + 1, len(jobs) - 1 
        m = (l + r) // 2
        while l <= r:
            if jobs[m][0] >= jobs[idx][1] and jobs[m-1][0] < jobs[idx][1]:
                next_idx = m
                break
            elif jobs[m][0] < jobs[idx][1]:
                l = m + 1
            else:
                r = m - 1
            m =  (l + r) // 2
        if next_idx:
            dp[idx] = max(jobs[idx][2] + dp[next_idx], dp[idx + 1])
        else:
            dp[idx] = max(jobs[idx][2], dp[idx+1])
        
    return dp[0]