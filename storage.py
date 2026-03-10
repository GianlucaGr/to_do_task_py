import json
from task_class import *


def save_tasks(taskList):
    data = [task.to_dict() for task in taskList]
    with open("tasks.json", "w") as file:
        json.dump(data,file,indent=4)
        
def load_tasks():
    try:
        with open("tasks.json","r") as file:
            data = json.load(file)
        
        taskList = []
        
        for item in data:
            task = Task.from_dict(item)
            taskList.append(task)

        return taskList
    except:
        FileNotFoundError
        return []
        
        
    


