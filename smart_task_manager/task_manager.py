# This file covers core logic for task management like adding, deleting, updating tasks

import json
import os
from utils import log_action

class TaskManager:
    def __init__(self, data_file='data/tasks.json'):
        self.data_file = data_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.data_file):
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            with open(self.data_file, 'w') as f:
                json.dump([], f)

        with open(self.data_file, 'r') as f:
            self.tasks = json.load(f)

    def save_tasks(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    @log_action("Add Task")
    def add_task(self, title, description, priority):
        task_id = self.get_next_id()
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "priority": priority.capitalize(),
            "completed": False
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task added (ID: {task_id})")

    def get_next_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        print("\n📝 Your Tasks:")
        for task in self.tasks:
            status = "✅" if task["completed"] else "❌"
            print(f"[{status}] ID: {task['id']} | {task['title']} ({task['priority']})")
            print(f"    Description: {task['description']}")

    @log_action("Mark Task Complete")
    def mark_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("⚠️ Task is already completed.")
                else:
                    task["completed"] = True
                    self.save_tasks()
                    print(f"✅ Task ID {task_id} marked as completed.")
                return
        print("❌ Task not found.")

    @log_action("Delete Task")
    def delete_task(self, task_id):
        original_count = len(self.tasks)
        self.tasks = list(filter(lambda task: task["id"] != task_id, self.tasks))

        if len(self.tasks) < original_count:
            self.save_tasks()
            print(f"🗑️ Task ID {task_id} deleted.")
        else:
            print("❌ Task not found.")
