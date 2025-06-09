import datetime
import sys

class Task:
    id=0
    def __init__(self, name):
        Task.id += 1
        self.id = Task.id
        self.name = name
        self.status = "todo"
        self.createdAt = datetime.datetime.now()
        self.updatedAt = datetime.datetime.now()
        
    def adding(self):
        print(f"Task added successfully (ID: {self.id})")
    
    def updating(self, name):
        self.name = name
        print(f"Task updated successfully (ID: {self.id})")
        
    def mark_in_progress(self):
        self.status = "in-progress"
        self.updatedAt = datetime.datetime.now()
        print(f"Task (ID: {self.id}) marked as in-progress")

    def mark_done(self):
        self.status = "done"
        self.updatedAt = datetime.datetime.now()
        print(f"Task (ID: {self.id}) marked as done")        
        
helptext = ('''Input your command:
add <taskname>
update <taskid> <newtaskname>
delete <taskid>
mark-in-progress <taskid>
mark-done <taskid>
list (<done, todo, in-progress>)
''')
def main():
    command = input(helptext)

    commandparts = command.split()
    def findTask():
        global tasks    
        try:
            taskId = int(commandparts[1])
        except:
            print("ID should be integer")
            return None   

        return tasks[taskId] if taskId in tasks else None
            
    match commandparts[0]:
            case "add":
                task = Task(commandparts[1])
                task.adding()  
            case "update":
                    newtaskname = commandparts[2]
                    if findTask():
                        findTask.updating(newtaskname)
                    else:
                        print(f"Task with ID {commandparts[1]} not found.")
            case "delete":
                deleteId = findTask()
                print(deleteId)
                if findTask():
                    del tasks[int(deleteId)]
                print(f"Task deleted successfully (ID: {command.id})")
                del command
            case "quit":
                quit()
            case _:
                print("Command is not valid")
                return
if __name__ == "__main__":
    tasks = {}
    main()