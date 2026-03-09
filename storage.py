import json
from task_class import *


def save_tasks(taskList):
    data = []
    for task in taskList:
        data.append({
            "task_id": task.task_id,
            "description": task.description,
            "complete": task.complete
        })
    with open("tasks.json", "w") as file:
        json.dump(data,file,indent=4)
        
def load_tasks():
    try:
        with open("tasks.json","r") as file:
            data = json.load(file)
        
        taskList = []
        
        for item in data:
            task = Task(item["description"])
            task.task_id = item["task_id"]
            task.complete = item["complete"]
        
            taskList.append(task)
        return taskList
    except:
        FileNotFoundError
        return []
        
        
    


