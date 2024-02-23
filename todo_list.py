class todo_List:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = " [X]" if task["completed"] else " [ ]"
                print(f"{i}. {task['task']}{status}")
        else:
            print("No tasks.")

    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task")

    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task")


def main():
    todo_list = todolList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_index)
        else choice == '5':
            print("Exiting")
            break
  


if __name__ == "__main__":
    main()
