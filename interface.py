import tkinter as tk
from tkinter import ttk

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style()
        style.theme_use("clam")  # allows more customization
        style.configure(
            "Title.TLabel",
            background="#f7f7f9",
            foreground="black"
        )

        # Button Font Style
        style.configure("Add.TButton",
                        font=("Arial", 14, "bold"),
                        background="#f7f7f9",
                        foreground="black")

        self.title("To-Do List App")
        self.geometry("850x850")
        self.configure(bg="#f7f7f9")

        self.columnconfigure(0, weight=1)
        self.title_text = ttk.Label(self, text="To-Do List",
                                    font=("Arial", 25, "bold"),
                                    style="Title.TLabel")
        self.title_text.grid(row=0, column=0, columnspan=3, pady=20)
        # --------------
        # FIELD SPACE
        # _-_-_-_-_-_-_-
        self.field_frame = ttk.Frame(self, padding=10, relief="solid", borderwidth=1, style="Title.TLabel")
        self.field_frame.columnconfigure(0, weight=3) # Task wider
        self.field_frame.columnconfigure(1, weight=1) # Priority
        self.field_frame.columnconfigure(2, weight=1) # Date
        self.field_frame.columnconfigure(3, weight=1) # Category
        self.field_frame.columnconfigure(4, weight=1) # Add button

        self.field_frame.grid(row=1, column=0, columnspan=3, padx=30, pady=20, sticky="ew")

        self.field_title = ttk.Label(self.field_frame, text="Add New Task",
                                     font=("Arial", 16, "bold"),
                                     foreground="#0d53d1",
                                     background="#f7f7f9")
        self.field_title.grid(row=0, column=0, columnspan=4, sticky="w", pady=10)

        # Task Entry
        self.task_entry_text = ttk.Label(self.field_frame,
                                         text="Task", background="#f7f7f9")
        self.task_entry_text.grid(row=1, column=0, sticky="w")
        self.task_entry = ttk.Entry(self.field_frame, width=30)
        self.task_entry.grid(row=2, column=0, sticky="ew")

        # Priority
        self.priority_entry_text = ttk.Label(self.field_frame,
                                         text="Priority", background="#f7f7f9")
        self.priority_entry_text.grid(row=1, column=1, sticky="w", padx= 10)
        self.priority_entry = ttk.Combobox(self.field_frame,
                                           width=10,
                                           values=["Low", "Medium", "High"],
                                           state="readonly")
        self.priority_entry.grid(row=2, column=1, padx= 10, sticky="ew")

        # Date Entry
        self.date_entry_text = ttk.Label(self.field_frame,
                                         text="Date", background="#f7f7f9")
        self.date_entry_text.grid(row=1, column=2, sticky="w")
        self.date_entry = ttk.Entry(self.field_frame, width=10)
        self.date_entry.grid(row=2, column=2, sticky="ew")

        # Category Entry
        self.category_entry_text = ttk.Label(self.field_frame,
                                         text="Category", background="#f7f7f9")
        self.category_entry_text.grid(row=1, column=3, sticky="w", padx= 10)
        self.category_entry = ttk.Combobox(self.field_frame,
                                           width=10,
                                           values=["General","Personal", "Work", "Study"],
                                           state="readonly")
        self.category_entry.grid(row=2, column=3, padx= 10, sticky="ew")

        # Add Task Button
        self.add_btn = ttk.Button(self.field_frame, text= "Add Task",
                                  style="Add.TButton")
        self.add_btn.grid(row=2, column=4)

        # ------------------------------
        # OTHER BUTTONS SPACE
        # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        self.button_frame = ttk.Frame(self, style="Title.TLabel")
        self.button_frame.columnconfigure(0, weight=1) # Completed button
        self.button_frame.columnconfigure(1, weight=1) # Delete button
        self.button_frame.columnconfigure(2, weight=1) # Edit button
        self.button_frame.columnconfigure(3, weight=1) # Clear button
        self.button_frame.grid(row=2, column=0, columnspan=4, sticky="ew")
        # Complete Button
        self.complete_btn = ttk.Button(self.button_frame, text= "Mark Complete",
                                  style="Add.TButton", padding=10)
        self.complete_btn.grid(row=0, column=0)
        # Delete button
        self.delete_btn = ttk.Button(self.button_frame, text= "Delete Task",
                                  style="Add.TButton", padding=10)
        self.delete_btn.grid(row=0, column=1)
        # Edit button
        self.edit_btn = ttk.Button(self.button_frame, text= "Edit Task",
                                  style="Add.TButton", padding=10)
        self.edit_btn.grid(row=0, column=2)
        # Clear button
        self.clear_btn = ttk.Button(self.button_frame, text= "Clear All",
                                  style="Add.TButton", padding=10)
        self.clear_btn.grid(row=0, column=3)

        # ------------------------------
        # Task Table
        # ------------------------------
        self.columns = ("Task", "Priority", "Due Date", "Category", "Status")

        self.table_frame = ttk.Frame(self)
        self.table_frame.grid(
            row=3,
            column=0,
            columnspan=4,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.rowconfigure(3, weight=1)

        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.rowconfigure(0, weight=1)

        self.task_table = ttk.Treeview(
            self.table_frame,
            columns=self.columns,
            show="headings",
            height=8
        )

        for col in self.columns:
            self.task_table.heading(col, text=col)

        self.task_table.column("Task", width=300, anchor="w")
        self.task_table.column("Priority", width=120, anchor="center")
        self.task_table.column("Due Date", width=140, anchor="center")
        self.task_table.column("Category", width=140, anchor="center")
        self.task_table.column("Status", width=140, anchor="center")

        self.task_table.grid(row=0, column=0, sticky="nsew")