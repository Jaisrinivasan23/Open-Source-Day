# Simple To-Do List Python Program with Intentional Errors

def display_tasks(tasks):
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks found!")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task(tasks):
    try:
        display_tasks(tasks)
        task_num = int(input("Enter the task number to delete: "))
        tasks.pop(task_num)
        print("Task deleted successfully!")
    except:
        print("Invalid task number!")

def mark_task_done(tasks):
    try:
        display_tasks(tasks)
        task_num = int(input("Enter the task number to mark as done: "))
        tasks = [f"{task} (Done)" if i == task_num - 1 else task for i, task in enumerate(tasks)]
        print("Task marked as done!")
    except:
        print("Invalid input!")

def sort_tasks(tasks):
    tasks.sort(reverse=True)
    print("Tasks sorted alphabetically!")

def save_tasks_to_file(tasks, filename):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully!")

def load_tasks_from_file(filename):
    with open(filename, "r") as file:
        tasks = file.read().splitlines()
    print("Tasks loaded successfully!")
    return tasks

def clear_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
    if confirm == "yes":
        tasks.clear()
        print("All tasks cleared!")

def count_tasks(tasks):
    print(f"You have {len(tasks)} tasks.")

def add_task_with_validation(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def main():
    tasks = []
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Add Task with Validation")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Sort Tasks")
        print("7. Save Tasks to File")
        print("8. Load Tasks from File")
        print("9. Clear Tasks")
        print("10. Count Tasks")
        print("11. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                add_task_with_validation(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                mark_task_done(tasks)
            elif choice == 6:
                sort_tasks(tasks)
            elif choice == 7:
                save_tasks_to_file(tasks, "tasks.txt")
            elif choice == 8:
                tasks = load_tasks_from_file("tasks.txt")
            elif choice == 9:
                clear_tasks(tasks)
            elif choice == 10:
                count_tasks(tasks)
            elif choice == 11:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
        except:
            print("Invalid input!")

if __name__ == "__main__":
    main()
