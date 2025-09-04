def main():
    tasks=[]
    while True:
        print("\n======== To Do List ========")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark Task is Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice =input("Enter your Choice:")
        if choice=='1':
            print()
            n_task=int(input("How many task you want to Add:"))

            for i in range(n_task):
                task_name =input("Enter the task:")
                tasks.append({"task": task_name, "done": False})
                print("====Task added====")   
        
        elif choice=='2':
            if not tasks:
                print("No tasks available. ")
                print("\nTasks:")
            for i, task in enumerate(tasks, 1):
                status="✔" if task["done"] else "❌"
                print(f"{i}. {task['task']} [{status}]")

        elif choice=='3':
            if not tasks:
                print("No tasks to mark complete.")        
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status="✔"  if task["done"] else "❌"  
                    print(f"{i}. {task['task']} [{status}]")
                num=int(input("Enter task number to mark complete:"))
                if 1<=num<=len(tasks):
                        tasks[num-1]["done"]=True
                       
                        print("Task marked as Complete!")
                else:
                        print("Invalid tsk number.")
        elif choice=='4':
            if not tasks:
                print("No tasks to delete.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status="✔"  if task["done"] else "❌"  
                    print(f"{i}. {task['task']} [{status}]")
                num=int(input("Enter task number to delete:"))
                if 1<=num<=len(tasks): 
                        removed=tasks.pop(num -1)
                        print(f"Task '{removed['task']}' deleted.")
                else:
                        print("Invalid tas number.")    

        elif choice=='5':
            print("Exiting....") 
            break
        else:
            print("Invalid choice. Try again.")   


                
main()
