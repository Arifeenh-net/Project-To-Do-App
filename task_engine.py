from tkinter import messagebox
from datetime import datetime

class TaskEngine:
    def __init__(self, ui):
        self.ui = ui
    def completed(self):
        selected = self.ui.task_table.selection()
        if not selected:
            return
        item_id = selected[0]
        values = list(self.ui.task_table.item(item_id, "values"))
        values[4] = "Completed"
        self.ui.task_table.item(item_id, values = values)
        self.completed_count()
        self.pending_count()
        self.save_task()

    def add_task(self):
        task = self.ui.task_entry.get()
        priority = self.ui.priority_entry.get()
        due_date = self.ui.date_entry.get()
        category = self.ui.category_entry.get()

        if priority == "High":
            priority_display = "🔴 High"
        elif priority == "Medium":
            priority_display = "🟡 Medium"
        else:
            priority_display = "🟢 Low"

        row_count = len(self.ui.task_table.get_children())

        if row_count % 2 == 0:
            row_tag = "evenrow"
        else:
            row_tag = "oddrow"

        if task.strip() == "" or priority == "" or due_date == "" or category == "":
            messagebox.showerror("Error", "You cannot leave any field empty")
        elif not self.valid_date(due_date):
            messagebox.showerror("Error", "Date must be written in DD-MM-YYY format!\n"
                                          "Ex: 20-11-2026")
        else:
            self.ui.task_table.insert("", "end",
                                      values=(task, priority_display, due_date, category, "Pending"),
                                      tags=row_tag)
            self.save_task()
            self.count_tasks()
            self.pending_count()
    def delete_task(self):
        selected = self.ui.task_table.selection()
        if selected:
           self.ui.task_table.delete(selected[0])
           self.save_task()
           self.count_tasks()
           self.completed_count()
           self.pending_count()
        else:
            messagebox.showerror("Error", "There is no task to delete!")

    def edit_task(self):
        selected = self.ui.task_table.selection()

        if not selected:
            messagebox.showerror("Error", "You must selected a task to edit!")
            return

        self.selected_item = selected[0]

        values = self.ui.task_table.item(self.selected_item, "values")

        self.ui.task_entry.delete(0, "end")
        self.ui.task_entry.insert(0, values[0])

        self.ui.priority_entry.set(values[1])

        self.ui.date_entry.delete(0, "end")
        self.ui.date_entry.insert(0, values[2])

        self.ui.category_entry.set(values[3])

        self.ui.add_btn.config(text="Update Task",
                               bootstyle="warning",
                               command=self.update_task)


    def update_task(self):
        task = self.ui.task_entry.get()
        priority = self.ui.priority_entry.get()
        due_date = self.ui.date_entry.get()
        category = self.ui.category_entry.get()

        if task.strip() == "" or priority == "" or due_date == "" or category == "":
            messagebox.showerror("Error", "You cannot leave any field empty!")
        elif not self.valid_date(due_date):
            messagebox.showerror("Error", "Date must be written in DD-MM-YYY format!\n"
                                          "Ex: 20-11-2026")
        else:
            self.ui.task_table.item(
                self.selected_item,
                values=(task, priority, due_date, category, "Pending")
            )

            self.ui.task_entry.delete(0, "end")
            self.ui.priority_entry.set("")
            self.ui.date_entry.delete(0, "end")
            self.ui.category_entry.set("")

            self.ui.add_btn.config(text="+ Add Task",
                                   bootstyle="primary",
                                   command=self.add_task)
            self.save_task()
            self.completed_count()
            self.pending_count()
    def clear(self):
        self.ui.task_entry.delete(0, "end")
        self.ui.priority_entry.set("")
        self.ui.date_entry.delete(0, "end")
        self.ui.category_entry.set("")

    def save_task(self):
        with open("tasks.txt", 'w') as file:

            for item in self.ui.task_table.get_children():
                values = self.ui.task_table.item(item, "values")

                file.write(",".join(values) + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    values = line.strip().split(",")
                    row_count = len(self.ui.task_table.get_children())
                    row_tag = "evenrow" if row_count % 2 == 0 else "oddrow"
                    self.ui.task_table.insert(
                        "",
                        "end",
                        values=values,
                        tags = row_tag
                    )
        except FileNotFoundError:
            pass

    def count_tasks(self):
        self.ui.total_count.config(
            text=f"Total Tasks: {len(self.ui.task_table.get_children())}"
        )

    def completed_count(self):
        total_completed = 0
        for item in self.ui.task_table.get_children():
            values = self.ui.task_table.item(item, "values")
            if values[4] == "Completed":
                total_completed += 1
        self.ui.completed_count.config(text=f"Completed Tasks: {total_completed}")

    def pending_count(self):
        total_completed = 0
        for item in self.ui.task_table.get_children():
            values = self.ui.task_table.item(item, "values")
            if values[4] == "Pending":
                total_completed += 1
        self.ui.pending_count.config(text=f"Pending Tasks: {total_completed}")

    def valid_date(self, date_text):
        try:
            datetime.strptime(date_text, "%d-%m-%Y")
            return True
        except ValueError:
            return False


