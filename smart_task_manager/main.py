# This is entry point of our application

from task_manager import TaskManager
from utils import get_motivational_quote

def show_menu():
    print("*********************************************")
    print("******Your personal SMART TASK MANAGER ******")
    print("*********************************************")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Get Motivation")
    print("6. Exit")
    print("*********************************************")

def main():
    tm = TaskManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            desc = input("Enter task description: ")
            priority = input("Enter task priority (Low/Medium/High): ")
            tm.add_task(title, desc, priority)
        elif choice == '2':
            tm.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            tm.mark_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            tm.delete_task(task_id)
        elif choice =='5':
            get_motivational_quote()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
