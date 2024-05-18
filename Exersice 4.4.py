sick_days = [10, 4, 5, 19]
for num in sick_days:
    if num > 0:
        total_sick_days = sum(sick_days)
        work_days = 365 - total_sick_days
        print(work_days)
    else:
        print("Frank can't be sick for -1 days!")
   