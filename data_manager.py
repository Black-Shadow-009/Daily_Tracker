import csv
c=0
datafile=open("data.csv", "r")
data=csv.reader(datafile)
slp= 0
"""for row in data:
    print(row[1])
    len(row)"""

## log a new data entry
def log_data():
    date=input("Today's date (YYYY-MM-DD): ")
    sleep=input("How many hours did you sleep last night? ")
    work=input("How many hours did you work for today? ")
    exercise=input("How many hours did you exercise for today? ")
    task_p=input("How many tasks are for today? ")
    task_c=input("How many tasks did you complete today? ")
    mood=input("How well is your mood today? (1-10) ")
    print("Data logged successfully!")
    with open("data.csv", "a") as datafile:
        data=csv.writer(datafile)
        data.writerow([date, sleep, work, exercise, task_p, task_c, mood])


def data_analysis():
    
    i, sleep, taskp, taskc, sleepreview, workdone= 0,0,0,0,"",""
    for row in data:
        sleep += eval(row[1])
        i+=1

        taskp += eval(row[4])
        taskc += eval(row[5])

    ### A quality sleep is around 7-8 hours.
    if sleep/i > 7 and sleep/i <=9: sleepreview="quality qleep"
    elif sleep/i <= 7 : sleepreview="bad sleep schedule"
    elif sleep/i >9: sleepreview= "sleep too much!"
    print(f"You're having {sleepreview}")
    
    ### Work done is efficient if its ratio is above 80%
    w = (taskc/taskp)*100
    if w >=80: workdone = "are doing consistent!"
    elif w < 80 and w >= 70 : workdone="are doing good!"
    elif w <= 70 : workdone= "lazy!"
    print(f"You're {workdone}" )


data_analysis()
