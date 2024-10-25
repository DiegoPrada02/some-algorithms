class Job:
    def __init__(self, profit, deadline):
        self.profit = profit
        self.deadline = deadline

def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    max_deadline = max(job.deadline for job in jobs)
    
    # Create a slots array to keep track of free time slots
    slots = [False] * (max_deadline + 1)  # Index 0 is not used
    total_profit = 0
    
    for job in jobs:
        # Find a free slot for this job
        for t in range(min(job.deadline, max_deadline), 0, -1):
            if not slots[t]:  # If the slot is free
                slots[t] = True  # Schedule the job
                total_profit += job.profit  # Add profit of this job
                break
    
    return total_profit

# Example usage
jobs = [Job(100, 2), Job(19, 1), Job(27, 2), Job(25, 1), Job(15, 3)]
max_profit = job_scheduling(jobs)
print(f"Max profit = {max_profit}")  # Output: 142
