class TasksCommand:
    TASKS_FILE = "tasks.txt"
    COMPLETED_TASKS_FILE = "completed.txt"

    current_items = {}
    completed_items = []

    def read_current(self):
        try:
            file = open(self.TASKS_FILE, "r")
            for line in file.readlines():
                item = line[:-1].split(" ")
                self.current_items[int(item[0])] = " ".join(item[1:])
            file.close()
        except Exception:
            pass

    def read_completed(self):
        try:
            file = open(self.COMPLETED_TASKS_FILE, "r")
            self.completed_items = file.readlines()
            file.close()
        except Exception:
            pass

    def write_current(self):
        with open(self.TASKS_FILE, "w+") as f:
            f.truncate(0)
            print(self.current_items,"writing")
            for key in sorted(self.current_items.keys()):
                f.write(f"{key} {self.current_items[key]}\n")

    def write_completed(self):
        with open(self.COMPLETED_TASKS_FILE, "w+") as f:
            f.truncate(0)
            for item in self.completed_items:
                f.write(f"{item}\n")

    def run(self, command, args):
        self.read_current()
        self.read_completed()
        if command == "add":
            self.add(args)
        elif command == "done":
            self.done(args)
        elif command == "delete":
            self.delete(args)
        elif command == "ls":
            self.ls()
        elif command == "report":
            self.report()
        elif command == "help":
            self.help()

    def help(self):
        print(
            """Usage :-
$ python tasks.py add 2 hello world # Add a new item with priority 2 and text "hello world" to the list
$ python tasks.py ls # Show incomplete priority list items sorted by priority in ascending order
$ python tasks.py del PRIORITY_NUMBER # Delete the incomplete item with the given priority number
$ python tasks.py done PRIORITY_NUMBER # Mark the incomplete item with the given PRIORITY_NUMBER as complete
$ python tasks.py help # Show usage
$ python tasks.py report # Statistics"""
        )

    def add(self, args):
        if int(args[0]) in self.current_items.keys():
            args[0]=int(args[0])+1
            
        self.current_items[int(args[0])]=args[1]
        print(f'Added task: "{args[1]}" with priority {args[0]}')
        print(self.current_items,"added")
        print(max(sorted(self.current_items.keys()))+1)
        pass

    def done(self, args):
        if args in self.current_items:
            self.completed_items.append(self.current_items[args[0]])
            self.current_items.pop(args[0])
            print("Marked item as done.")
        else:
            print(f"Error: no incomplete item with priority {args[0]} exists.")
        pass

    def delete(self, args):
        print("Deleted item with priority "+args[0])
        pass

    def ls(self):
        j=1
        for i in self.current_items:
            print(self.current_items)
            print(f"{j}. {self.current_items[i]} [{i}]\n")
            j+=1
        pass

    def report(self):
        pass
