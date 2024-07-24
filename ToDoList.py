 
# Define a class Task to represent each task
class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.description}"


# Define a To-Do List class to manage tasks
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Task '{self.tasks[task_index].description}' marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def menu(self):
        while True:
            print("\n===== To-Do List Menu =====")
            print("1. Add Task")
            print("2. Mark Task as Completed")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                description = input("Enter task description: ")
                self.add_task(description)
            elif choice == '2':
                task_index = int(input("Enter task index to mark as completed: ")) - 1
                self.mark_completed(task_index)
            elif choice == '3':
                task_index = int(input("Enter task index to delete: ")) - 1
                self.delete_task(task_index)
            elif choice == '4':
                print("\n===== Tasks =====")
                self.show_tasks()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Main function to run the program
if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.menu()
