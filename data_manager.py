import csv
c=0
datafile=open("data.csv", "r")
data=csv.reader(datafile)

for row in data:
    print(row)

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