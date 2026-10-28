
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os


class StudentRecordManager:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Student Record Manager")
        self.root.geometry("850x700")
        self.root.minsize(750, 650)

        self.records = {}
        self.file_path = "students.json"

        self.roll_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Male")
        self.course_var = tk.StringVar(value="Computer Science")
        self.hobbies = {
            "Sports": tk.BooleanVar(),
            "Music": tk.BooleanVar(),
            "Reading": tk.BooleanVar()
        }

        self.create_widgets()
        self.load_default_file()

    def create_widgets(self):
        title = tk.Label(
            self.root,
            text="STUDENT RECORD MANAGER",
            font=("Arial", 20, "bold"),
            fg="navy"
        )
        title.pack(pady=10)

        form = ttk.LabelFrame(
            self.root,
            text="Student Details",
            padding=12
        )
        form.pack(fill="x", padx=15, pady=5)

        ttk.Label(form, text="Roll Number:").grid(
            row=0, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(form, textvariable=self.roll_var, width=30).grid(
            row=0, column=1, sticky="ew", padx=5, pady=5
        )

        ttk.Label(form, text="Name:").grid(
            row=1, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(form, textvariable=self.name_var, width=30).grid(
            row=1, column=1, sticky="ew", padx=5, pady=5
        )

        ttk.Label(form, text="Age:").grid(
            row=2, column=0, sticky="w", padx=5, pady=5
        )
        ttk.Entry(form, textvariable=self.age_var, width=30).grid(
            row=2, column=1, sticky="ew", padx=5, pady=5
        )

        ttk.Label(form, text="Gender:").grid(
            row=3, column=0, sticky="w", padx=5, pady=5
        )

        gender_frame = ttk.Frame(form)
        gender_frame.grid(row=3, column=1, sticky="w")

        for gender in ("Male", "Female", "Other"):
            ttk.Radiobutton(
                gender_frame,
                text=gender,
                variable=self.gender_var,
                value=gender
            ).pack(side="left", padx=5)

        ttk.Label(form, text="Course:").grid(
            row=4, column=0, sticky="w", padx=5, pady=5
        )

        courses = [
            "Computer Science",
            "Information Technology",
            "Electronics",
            "Mechanical",
            "Civil"
        ]

        ttk.Combobox(
            form,
            textvariable=self.course_var,
            values=courses,
            state="readonly",
            width=27
        ).grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(form, text="Hobbies:").grid(
            row=5, column=0, sticky="nw", padx=5, pady=5
        )

        hobby_frame = ttk.Frame(form)
        hobby_frame.grid(row=5, column=1, sticky="w")

        for hobby, variable in self.hobbies.items():
            ttk.Checkbutton(
                hobby_frame,
                text=hobby,
                variable=variable
            ).pack(side="left", padx=5)

        ttk.Label(form, text="Address / Remarks:").grid(
            row=6, column=0, sticky="nw", padx=5, pady=5
        )

        self.remarks_text = tk.Text(form, height=3, width=35)
        self.remarks_text.grid(
            row=6, column=1, sticky="ew", padx=5, pady=5
        )

        form.columnconfigure(1, weight=1)

        # Action buttons
        buttons = ttk.Frame(self.root)
        buttons.pack(fill="x", padx=15, pady=10)

        actions = [
            ("Add / Update", self.add_record),
            ("Retrieve", self.retrieve_record),
            ("Delete", self.delete_record),
            ("Clear", self.clear_form),
            ("Open File", self.open_file),
            ("Save As", self.save_as)
        ]

        for text, command in actions:
            ttk.Button(
                buttons, text=text, command=command
            ).pack(side="left", padx=4, pady=4, expand=True, fill="x")

        # Student records table
        table_frame = ttk.LabelFrame(
            self.root,
            text="Saved Student Records",
            padding=8
        )
        table_frame.pack(fill="both", expand=True, padx=15, pady=5)

        columns = ("roll", "name", "age", "gender", "course")
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        headings = {
            "roll": "Roll Number",
            "name": "Name",
            "age": "Age",
            "gender": "Gender",
            "course": "Course"
        }

        for column, heading in headings.items():
            self.tree.heading(column, text=heading)
            self.tree.column(column, width=120, anchor="center")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.select_record)

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(
            self.root,
            textvariable=self.status_var,
            relief="sunken",
            anchor="w"
        ).pack(fill="x", side="bottom")

    def load_default_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    self.records = json.load(file)
                self.refresh_table()
                self.status_var.set(
                    f"Loaded {len(self.records)} student record(s)"
                )
            except (json.JSONDecodeError, OSError) as error:
                messagebox.showerror(
                    "File Error",
                    f"Could not load student records:\n{error}"
                )

    def save_records(self):
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(self.records, file, indent=4)
            self.status_var.set(f"Saved to {self.file_path}")
            return True
        except OSError as error:
            messagebox.showerror("Save Error", str(error))
            return False

    def add_record(self):
        roll = self.roll_var.get().strip()
        name = self.name_var.get().strip()
        age_text = self.age_var.get().strip()

        if not roll or not name or not age_text:
            messagebox.showwarning(
                "Missing Details",
                "Enter roll number, name, and age."
            )
            return

        try:
            age = int(age_text)
            if age <= 0 or age > 120:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid Age",
                "Age must be a number between 1 and 120."
            )
            return

        record = {
            "roll": roll,
            "name": name,
            "age": age,
            "gender": self.gender_var.get(),
            "course": self.course_var.get(),
            "hobbies": [
                hobby for hobby, variable in self.hobbies.items()
                if variable.get()
            ],
            "remarks": self.remarks_text.get("1.0", "end-1c").strip()
        }

        if roll in self.records:
            update = messagebox.askyesno(
                "Update Record",
                "This roll number already exists. Update the record?"
            )
            if not update:
                return

        self.records[roll] = record

        if self.save_records():
            self.refresh_table()
            messagebox.showinfo(
                "Success",
                "Student record saved successfully."
            )

    def retrieve_record(self):
        roll = self.roll_var.get().strip()

        if not roll:
            messagebox.showwarning(
                "Input Required",
                "Enter a roll number to retrieve a record."
            )
            return

        record = self.records.get(roll)

        if record is None:
            messagebox.showinfo(
                "Not Found",
                "No student record found for this roll number."
            )
            return

        self.display_record(record)
        messagebox.showinfo("Success", "Student record retrieved.")

    def display_record(self, record):
        self.clear_form()

        self.roll_var.set(record["roll"])
        self.name_var.set(record["name"])
        self.age_var.set(str(record["age"]))
        self.gender_var.set(record.get("gender", "Male"))
        self.course_var.set(record.get("course", "Computer Science"))

        saved_hobbies = record.get("hobbies", [])
        for hobby, variable in self.hobbies.items():
            variable.set(hobby in saved_hobbies)

        self.remarks_text.insert("1.0", record.get("remarks", ""))

    def delete_record(self):
        roll = self.roll_var.get().strip()

        if not roll:
            selected = self.tree.selection()
            if selected:
                roll = self.tree.item(selected[0], "values")[0]

        if not roll or roll not in self.records:
            messagebox.showwarning(
                "Not Found",
                "Select a student or enter a valid roll number."
            )
            return

        if messagebox.askyesno(
            "Confirm Delete",
            f"Delete student record {roll}?"
        ):
            del self.records[roll]

            if self.save_records():
                self.refresh_table()
                self.clear_form()
                messagebox.showinfo(
                    "Deleted",
                    "Student record deleted successfully."
                )

    def select_record(self, event=None):
        selected = self.tree.selection()
        if selected:
            roll = self.tree.item(selected[0], "values")[0]
            record = self.records.get(roll)
            if record:
                self.display_record(record)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for roll, record in sorted(self.records.items()):
            self.tree.insert(
                "",
                "end",
                values=(
                    roll,
                    record["name"],
                    record["age"],
                    record["gender"],
                    record["course"]
                )
            )

    def clear_form(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.gender_var.set("Male")
        self.course_var.set("Computer Science")

        for variable in self.hobbies.values():
            variable.set(False)

        self.remarks_text.delete("1.0", "end")

    def open_file(self):
        filename = filedialog.askopenfilename(
            title="Open Student Records",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if not filename:
            return

        try:
            with open(filename, "r", encoding="utf-8") as file:
                loaded = json.load(file)

            if not isinstance(loaded, dict):
                raise ValueError("The JSON file must contain a record dictionary.")

            for roll, record in loaded.items():
                if not isinstance(record, dict):
                    raise ValueError(f"Invalid record for roll number {roll}.")

                if not all(key in record for key in ("roll", "name", "age", "gender", "course")):
                    raise ValueError(f"Incomplete record for roll number {roll}.")

            self.records = loaded
            self.file_path = filename
            self.refresh_table()
            self.clear_form()
            self.status_var.set(f"Opened {filename}")
            messagebox.showinfo("Success", "Records loaded successfully.")

        except (OSError, json.JSONDecodeError, ValueError) as error:
            messagebox.showerror("Open Error", str(error))

    def save_as(self):
        filename = filedialog.asksaveasfilename(
            title="Save Student Records",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")]
        )

        if filename:
            old_path = self.file_path
            self.file_path = filename

            if self.save_records():
                messagebox.showinfo(
                    "Success",
                    f"Records saved to:\n{filename}"
                )
            else:
                self.file_path = old_path


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordManager(root)
    root.mainloop()
