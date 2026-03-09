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