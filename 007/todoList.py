'''
Caleb Thomas 
03/12/25
Project Description:
Create a simple To-Do List Manager where users can:

1. Add tasks to their list.
2. Remove completed tasks.
3. View all tasks.
4. Reorder tasks.
5. Exit the program.
'''

#TODO - make a input gui for the user to interact with the program

# Import the necessary modules
import ToDoController as controller

def startup():
    """
    Starts the program
    @returns: None
    """
    task_list = []
    while True:
        print("\n\n")
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Reorder Tasks")
        print("5. Mark Tasks As Complete")
        print("6. Exit")
        choice = int(input("Enter the number of the action you want to do: "))
        if choice == 1:
            task = input("Enter the task you want to add: ")
            task_list = controller.add_task(task, task_list)
        elif choice == 2:
            task = input("Enter the task you want to remove: ")
            task_list = controller.remove_task(task, task_list)
        elif choice == 3:
            controller.view_tasks(task_list)
        elif choice == 4:
            task_list = controller.reorder_tasks(task_list)
        elif choice == 5:
            new_list = controller.mark_task_complete(task_list)
            task_list = new_list
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


