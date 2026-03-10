class Task():
    contador_id = 1
    
    def __init__(self, description:str, id = None, tComplete:bool = False):
        self.description = description
        self.complete = tComplete

        if id is None:       # If the task is created on terminal
             self.task_id = Task.contador_id
             Task.contador_id += 1
        else:                # when task is loaded from json 
            self.task_id = id
            
            if id >= Task.contador_id:
                 Task.contador_id = id + 1
        
        
    def __repr__(self):
        if self.complete:
            return f"{self.task_id}. {self.description} -> Completa"
        else:
            return f"{self.task_id}. {self.description} -> Incompleta"
        
    def completeTask(self):
            self.complete = True

    def to_dict(self)->dict:
        task = {
             "task_id" : self.task_id,
             "description" : self.description,
             "complete" : self.complete
        }
        return task

    @classmethod 
    def from_dict(cls,data):

        return cls(
             data["description"],
             data["task_id"],
             data["complete"]
        )    