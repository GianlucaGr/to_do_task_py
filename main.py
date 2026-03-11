from task_class import *
from storage import *

def main():
    taskList = load_tasks() #this function loads json tasks
    
    while True:
        print("-------------------")
        print("1. Add a task")
        print("2. See tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5 Exit")
        print("-------------------")

        try: # if the input is not a number, send a advice and repeat
            option = int(input("Choose one option: "))
        
        except ValueError:
            print("\nEnter a number please")
            continue
        
        if option not in[1,2,3,4,5]:
            print("\nPlease enter a valid option from the menu!")
            
        print("-------------------")
    
    
        afterInput(option,taskList) 


def afterInput(option:int,taskList:list)->any:
    description = None

    if option == 1: #Add a task
        description = str(input("Describe task :"))
        taskList.append(Task(description))
        save_tasks(taskList)
        printList(taskList)
        
    elif option == 2: #See tasks
        printList(taskList)

    elif option == 3: #Complete task
        try: 
            taskId = int(input("Choose the task number :"))
            findTaskAndComplete(taskId,taskList)
            save_tasks(taskList)
        except ValueError:
            print("\n Choose a number please")
            return

    elif option == 4: #Delete task
        try:
            delTs = int(input("Choose the task to delete : "))
            deleteTask(delTs,taskList)
            save_tasks(taskList)
        except ValueError:
            print("\n Choose a number please")
            return
        
    elif option == 5:
        exit()

def printList(tasklist:list)-> any:

    print(" ")
    print("Tasker:")
    for task in tasklist:
        print(task)
    print(" ")

def findTaskAndComplete(taskId: int, tasklist: list):

    for task in tasklist:
        if task.task_id == taskId:
            task.completeTask()
            print(f"\nTask number {task.task_id} was complete! ")
            return
    print("\nTask not found!") # if taskId is not found in list, send an advice


def deleteTask(delTs:int,tasklist:list)-> any:
    for task in tasklist:
        if task.task_id == delTs:
            if task.complete: 
                tasklist.remove(task)
                print("\nTask deleted")
            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print("\nThe task is not complete")
                print("!!!!!!!!!!!!!!!!!!!!")
        
            return
        
    print("!!!!!!!!!!!!!!!!!!!!")
    print("\nThat task number doesnt exist")# if delTs is not found in list, send an advice
    print("!!!!!!!!!!!!!!!!!!!!")

main()




