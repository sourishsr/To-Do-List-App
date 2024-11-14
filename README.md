A simple to-do list app where users can add, view, and remove tasks. Store the list of tasks in a text file so that it persists between app sessions.

Add tasks: Users can add new tasks to the list.
View tasks: Users can view all the tasks.
Mark tasks as completed: Users can mark tasks as completed.
Delete tasks: Users can delete tasks from the list.
Save tasks to a file: Tasks are stored in a text file so they persist between app sessions.

How It Works:
Task Storage: Tasks are stored in a file called tasks.txt. If the file exists, the program loads tasks from it when the app starts.
Viewing Tasks: The view_tasks function displays all the current tasks. Each task is numbered for easy reference.
Adding Tasks: Users can add a task by entering it, which is appended to the task list.
Completing Tasks: Users can mark a task as completed by entering its number. The task is updated with a "(Completed)" tag.
Deleting Tasks: Users can delete a task by selecting its number. The task is removed from the list.
Saving Tasks: When the user exits the app, the tasks are saved back into the tasks.txt file, so they persist between app sessions.

Key Features:
Persistence: The tasks are saved in a text file (tasks.txt), so they remain even after closing the app.
User-Friendly: It provides simple text-based navigation for viewing, adding, completing, and deleting tasks.
Data Validation: It ensures that invalid task numbers are handled gracefully.
