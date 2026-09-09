def task_scheduling(tasks):
    print("\nTASK SCHEDULE PROBLEM")
    print("-----------------------")

    previous_finish = 0

    for task in tasks:
        task_number = task[0]
        start_time = task[1]
        finish_time = task[2]

        if start_time >= previous_finish:
            print("Task", task_number, "is scheduled.")
            print("Start Time:", start_time)
            print("Finish Time:", finish_time)

            previous_finish = finish_time

        else:
            print("Task", task_number, "is not scheduled.")
            print("Reason: It overlaps with the previous task.")

        print()


# Take input from user
n = int(input("Enter the number of tasks: "))

tasks = []

for i in range(n):
    print("\nEnter details of Task", i + 1)

    start_time = int(input("Enter the start time: "))
    finish_time = int(input("Enter the finish time: "))

    tasks.append((i + 1, start_time, finish_time))


# Sort tasks according to finish time
tasks.sort(key=lambda x: x[2])

# Call the function
task_scheduling(tasks)