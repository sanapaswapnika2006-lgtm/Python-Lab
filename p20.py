import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modular Multi-Frame Dashboard")
        self.root.geometry("800x500")
        self.root.minsize(600, 400)

        self.sidebar = tk.Frame(root, bg="#263238", width=180)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="MY DASHBOARD",
            bg="#263238",
            fg="white",
            font=("Arial", 14, "bold")
        ).pack(pady=25)

        self.content = tk.Frame(root, bg="#f4f6f8")
        self.content.pack(side="right", fill="both", expand=True)

        for page in ["Home", "Profile", "Settings"]:
            tk.Button(
                self.sidebar,
                text=page,
                font=("Arial", 12),
                command=lambda p=page: self.show_page(p)
            ).pack(fill="x", padx=12, pady=6)

        self.show_page("Home")

    def show_page(self, page):
        for widget in self.content.winfo_children():
            widget.destroy()

        if page == "Home":
            title = "Welcome to the Dashboard"
            description = "This is the Home page."
        elif page == "Profile":
            title = "User Profile"
            description = "Your profile information goes here."
        else:
            title = "Settings"
            description = "Dashboard settings go here."

        tk.Label(
            self.content,
            text=title,
            font=("Arial", 22, "bold"),
            bg="#f4f6f8"
        ).pack(pady=(70, 15))

        tk.Label(
            self.content,
            text=description,
            font=("Arial", 13),
            bg="#f4f6f8"
        ).pack(pady=10)

        if page == "Settings":
            tk.Button(
                self.content,
                text="Show Message",
                command=lambda: messagebox.showinfo(
                    "Settings", "Settings button works!"
                )
            ).pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()