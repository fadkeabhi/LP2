def schedule_jobs(currTime, jobs):
  if not jobs:
    return 0,list()
  
  profitWithCurrentExecuted = 0
  profitWithOutCurrentExecuted = 0

  jobsWithoutCurrent = jobs.copy()
  jobsWithoutCurrent.pop(0)
  currentJob = jobs[0]
  
  #check if current job can be completed in deadline
  if currentJob["time"] + currTime <= currentJob["deadline"]:
    newTime = currentJob["time"] + currTime
    profitWithCurrentExecuted, schedule = schedule_jobs(newTime, jobsWithoutCurrent)
    profitWithCurrentExecuted += currentJob["profit"]

  profitWithOutCurrentExecuted, schedule = schedule_jobs(currTime, jobsWithoutCurrent)

  if profitWithCurrentExecuted > profitWithOutCurrentExecuted:
    schedule.append(currentJob)
    return profitWithCurrentExecuted, schedule
  else:
    return profitWithOutCurrentExecuted, schedule
    


# Example usage
jobsList = [
    {'profit': 50, 'time': 3, 'deadline': 10},
    {'profit': 20, 'time': 1, 'deadline': 2},
    {'profit': 40, 'time': 5, 'deadline': 7},
]

jobsList.sort(key= lambda x:x["deadline"])

total_profit, schedule = schedule_jobs(0, jobsList)


schedule.reverse()

print("Total Profit:", total_profit)
print("Schedule:", [i['profit'] for i in schedule])