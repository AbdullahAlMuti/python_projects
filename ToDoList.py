print("\n""\n")
print("  Welcometo Task App")
print("=== === === === === === ")

tasks = []
while True:
    print("\n1. Display Tasks")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. Completed Tasks")
    print("5. Exit Application")

    choice = int(input("Choose between 1 -5 :"))

    if choice == 1:
        if tasks:
            print("Here are your tasks:")
            for task in tasks:
                print(task)
        else:
            print("No tasks are available")
    elif choice == 2:
        new_task =input("Add your task here : ")
        tasks.append(new_task)
        print("Task Added Succesfully")
    elif choice == 3:
        if tasks:
            remove_task = input("Enter the Task to Remove: ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                print("Task Remove Successfully")
            else:
                print("No Task founded !")
    elif choice == 4:
        if tasks:
            complete_task = input("Mark the task u wanna commplete.")
            if complete_task in tasks:
                tasks.remove(complete_task)
                print("Task Successfully Completed.")
            else:
                print("Tasks not found !")
    elif choice == 5:
        print("Exiting this Application")
        break