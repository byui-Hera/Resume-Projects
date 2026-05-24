tasks = []


def add_tasks():

    subject = input("Enter subject: ")
    task = input("Enter task: ")

    full_task = subject + " - " + task
    tasks.append(full_task)
    print("Task added!")



def view_tasks():

    if len(tasks) == 0:
        print("No task yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")



def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
        print("Task saved!")    



def remove_tasks():

    view_tasks()

    remove_tasks = int(input("Remove a task: "))
    tasks.pop(remove_tasks - 1)
    print("Task is removed!")


def main():

    while True: 
        print("---Study Tracker---")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Save Tasks")
        print("4. Remove Tasks")
        print("5. Quit")


        choice = input("Enter one of the choices above: ")

        if choice == "1":
            add_tasks()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            save_tasks()

        elif choice == "4":
            remove_tasks()
        
        elif choice == "5":
            save_tasks()
            print("Goodbye!")
            break

        else: 
            print("Invalid Response! Try again!")

main()






