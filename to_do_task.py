
def main():
    taskList = []
    
    while True:
        print("-------------------")
        print("1. Add a task")
        print("2. See tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5 Exit")
        print("-------------------")

        try:
            option = int(input("Choose one option: "))
        
        except ValueError:
            print("Enter a number please")
            continue
            
        print("-------------------")
    
    
        afterInput(option,taskList) 


def afterInput(option:int,taskList:list)->any:
    description = None

    if option == 1: #Add a task
        description = str(input("Describe task :"))
        taskList.append(Task(description))
        printList(taskList)
    if option == 2: #See tasks
        printList(taskList)
    if option == 3: #Complete task
        taskId = int(input("Choose the task number :"))
        findTaskAndComplete(taskId,taskList)
    if option == 4: #Delete task
        delTs = int(input("Choose the task to delete : "))
        deleteTask(delTs,taskList)
    if option == 5:
        exit()

class Task():
    contador_id = 1
    def __init__(self, description:str):
        self.description = description
        self.complete = False
        self.task_id = Task.contador_id
        Task.contador_id += 1 
    def __repr__(self):
        if self.complete:
            return f"{self.task_id}. {self.description} -> Completa"
        else:
            return f"{self.task_id}. {self.description} -> Incompleta"
        
    def completeTask(self):
            self.complete = True

def printList(tasklist:list)-> any:

    print("")
    print("##############")
    print("Tasker:")
    for task in tasklist:
        print(task)
    print("##############")
    print("")

def findTaskAndComplete(taskId: int, tasklist: list):

    for task in tasklist:
        if task.task_id == taskId:
            task.completeTask()
            print("")
            print(f"Task number {task.task_id} was complete! ")
            print("")
            return
    print("")
    print("Task not found!")
    print("")


def deleteTask(delTs:int,tasklist:list)-> any:
    for task in tasklist:
        if task.task_id == delTs:
            if task.complete: 
                tasklist.remove(task)
            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print("The task is not complete")
                print("!!!!!!!!!!!!!!!!!!!!")
            break
        else:
            print("!!!!!!!!!!!!!!!!!!!!")
            print("That task number doesnt exist")
            print("!!!!!!!!!!!!!!!!!!!!")
        break

main()




