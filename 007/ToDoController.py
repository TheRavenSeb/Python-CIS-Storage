
# Had to make single line comments as notebooks wasn't liking it when writing the module to a file
#Caleb Thomas
#03/12/25
#Project Description:
#Create a module that does the functions required to manage a to-do list program


#TODO - Create a function to add tasks to the list
#TODO - Create a function to remove tasks from the list
#TODO - Create a function to view all tasks
#TODO - Create a function to reorder tasks
#TODO - Create a function to exit the program


# Had to make single line comments as notebooks wasn't liking it when writing the module to a file
#Caleb Thomas
#03/12/25
#Project Description:
#Create a module that does the functions required to manage a to-do list program


#TODO - Create a function to add tasks to the list
#TODO - Create a function to remove tasks from the list
#TODO - Create a function to view all tasks
#TODO - Create a function to reorder tasks
#TODO - Create a function to exit the program


def add_task(task, task_list):
    """
    Adds a task to the list
    @param(String): task
    @param(List): task_list
    @returns: List
    """
    task_list.append(task)
    return task_list

def remove_task(task, task_list):
    """
    Removes a task from the list
    @param(String): task
    @param(List): task_list
    @returns: List
    """
    task_list.remove(task)
    return task_list

def view_tasks(task_list):
    """
    Views all tasks in the list
    @param(List): task_list
    @returns: None
    """
    index = 0
    
    print("Tasks:")
    if len(task_list) == 0:
        print("No tasks to display")
        return
    
    for task in task_list:
        print(f"{index}. {task}")
        index += 1
    
def reorder_tasks(task_list):
    """
    Reorders tasks in the list
    @param(List): task_list
    @returns: List
    """
    
    print("Reorder Tasks")
    view_tasks(task_list)
    task_index = int(input("Enter the index of the task you want to move: "))
    new_index = int(input("Enter the new index for the task: "))
    task = task_list.pop(task_index - 1)
    task_list.insert(new_index - 1, task)
    return task_list

def mark_task_complete(task_list):
    """
    Marks a task as complete
    
    @param(List): task_list
    @returns: List
    """
    try:
        view_tasks(task_list)
        
        taskNum = input(f"Enter the task you want to mark as complete (0 - {len(task_list)-1}): ")
        task = task_list[int(taskNum)]
        if task.endswith(" - Completed"):
            print("Task is already completed")
            return task_list
        
        task_list.remove(task)
        task_list.append(f"{task} - Completed")
        return task_list

    except ValueError:
        print(f"Invalid task number. Please enter a number between 0 and {len(task_list)-1}")
        return task_list  
        
         
        
        
        
         
        
        