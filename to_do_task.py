def main():
    taskList = []
    
    while True:
        print("1. Add a task")
        print("2. See tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5 Exit")

        option = int(input("Choose one option: "))
    
    
        afterInput(option,taskList)


def afterInput(option:int,taskListE:list)->any:
    taskList = taskListE
    task = None

    if option == 1: #Add a task
        task = str(input("Discribe task :"))
        taskList.append(Task(task))
        printList(taskList)
    if option == 2: #See tasks
        printList(taskList)
    if option == 3: #Complete task
        taskId = int(input("Choose the task number :"))
        findTask(taskId,taskList)
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
        if self.complete == True:
            return f"{self.task_id}. {self.description} -> Completa"
        else:
            return f"{self.task_id}. {self.description} -> Incompleta"
        
    def completeTask(self):
            self.complete = True

def printList(tasklist:list)-> any:
    taskList = tasklist
    for task in taskList:
        print(task)

def findTask(taskId:int,tasklist:list)-> any:
    taskList = tasklist
    for task in taskList:
        if task.task_id == taskId:
            task.completeTask()
    return printList(taskList)


def deleteTask(delTs:int,tasklist:list)-> any:
    taskList = tasklist
    for task in tasklist:
        if task.task_id == delTs: 
            tasklist.remove(task)
    return printList(taskList)

main()




