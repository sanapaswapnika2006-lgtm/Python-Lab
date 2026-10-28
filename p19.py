
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
import os

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class FileViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Image and File Viewer")
        self.root.geometry("800x600")
        self.root.minsize(500, 400)

        self.current_image = None
        self.photo = None
        self.current_file = ""

        # Title
        tk.Label(
            root,
            text="DYNAMIC IMAGE / FILE VIEWER",
            font=("Arial", 18, "bold"),
            bg="lightblue",
            pady=12
        ).pack(fill="x")

        # Buttons
        buttons = tk.Frame(root)
        buttons.pack(fill="x", padx=10, pady=8)

        tk.Button(
            buttons, text="Open Image",
            command=self.open_image
        ).pack(side="left", padx=4)

        tk.Button(
            buttons, text="Open Text File",
            command=self.open_text
        ).pack(side="left", padx=4)

        tk.Button(
            buttons, text="Choose Color",
            command=self.choose_color
        ).pack(side="left", padx=4)

        tk.Button(
            buttons, text="Clear",
            command=self.clear
        ).pack(side="left", padx=4)

        # File path entry
        path_frame = tk.Frame(root)
        path_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(path_frame, text="File path:").pack(side="left")

        self.path_entry = tk.Entry(path_frame)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=5)
        self.path_entry.bind("<Return>", self.open_path)

        tk.Button(
            path_frame,
            text="Open",
            command=self.open_path
        ).pack(side="right")

        # File information
        self.info = tk.Label(
            root, text="No file selected",
            anchor="w", padx=10
        )
        self.info.pack(fill="x", pady=4)

        # Display frame
        self.display_frame = tk.Frame(root, bg="white")
        self.display_frame.pack(
            fill="both", expand=True, padx=10, pady=5
        )

        # Image canvas
        self.canvas = tk.Canvas(
            self.display_frame,
            bg="white",
            highlightthickness=0
        )
        self.canvas.bind("<Configure>", self.resize_image)
        self.canvas.bind("<Button-1>", self.canvas_click)

        # Text display with scrollbar
        self.text_frame = tk.Frame(self.display_frame)

        self.text_box = tk.Text(
            self.text_frame,
            wrap="word",
            font=("Consolas", 11)
        )

        scrollbar = tk.Scrollbar(
            self.text_frame,
            command=self.text_box.yview
        )
        self.text_box.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        self.text_box.pack(side="left", fill="both", expand=True)

        # Status bar
        self.status = tk.Label(
            root,
            text="Ready",
            anchor="w",
            relief="sunken"
        )
        self.status.pack(fill="x", side="bottom")

        self.canvas.pack(fill="both", expand=True)

    def select_file(self, filetypes):
        filename = filedialog.askopenfilename(
            title="Select File",
            filetypes=filetypes
        )
        if filename:
            self.show_file(filename)

    def open_image(self):
        if not PIL_AVAILABLE:
            messagebox.showerror(
                "Missing Library",
                "Install Pillow first:\npython -m pip install Pillow"
            )
            return

        self.select_file([
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("All files", "*.*")
        ])

    def open_text(self):
        self.select_file([
            ("Text files", "*.txt *.csv *.log"),
            ("All files", "*.*")
        ])

    def open_path(self, event=None):
        filename = self.path_entry.get().strip()

        if not filename:
            messagebox.showwarning(
                "Missing Path", "Please enter a file path."
            )
            return

        if not os.path.isfile(filename):
            messagebox.showerror(
                "File Error", "File does not exist."
            )
            return

        self.show_file(filename)

    def show_file(self, filename):
        extension = os.path.splitext(filename)[1].lower()
        image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}

        try:
            if extension in image_extensions:
                if not PIL_AVAILABLE:
                    messagebox.showerror(
                        "Missing Library",
                        "Install Pillow:\npython -m pip install Pillow"
                    )
                    return

                with Image.open(filename) as img:
                    self.current_image = img.copy()

                self.text_frame.pack_forget()
                self.canvas.pack(fill="both", expand=True)
                self.current_file = filename
                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, filename)

                self.info.config(
                    text="Image: " + os.path.basename(filename)
                )
                self.display_image()
                self.status.config(text="Image opened successfully")

            else:
                with open(filename, "r", encoding="utf-8-sig") as file:
                    content = file.read()

                self.canvas.pack_forget()
                self.text_frame.pack(fill="both", expand=True)

                self.text_box.config(state="normal")
                self.text_box.delete("1.0", tk.END)
                self.text_box.insert("1.0", content)
                self.text_box.config(state="disabled")

                self.current_image = None
                self.current_file = filename

                self.path_entry.delete(0, tk.END)
                self.path_entry.insert(0, filename)

                self.info.config(
                    text="Text file: " + os.path.basename(filename)
                )
                self.status.config(text="Text file opened successfully")

        except (OSError, ValueError, UnicodeError) as error:
            messagebox.showerror(
                "Unable to Open File", str(error)
            )

    def display_image(self, event=None):
        if self.current_image is None:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width < 10 or height < 10:
            return

        image = self.current_image.copy()
        image.thumbnail((width - 20, height - 20))

        self.photo = ImageTk.PhotoImage(image)

        self.canvas.delete("all")
        self.canvas.create_image(
            width // 2,
            height // 2,
            image=self.photo,
            anchor="center"
        )

    def resize_image(self, event=None):
        if self.current_image is not None:
            self.display_image()

    def choose_color(self):
        result = colorchooser.askcolor(title="Choose Background Color")

        if result and result[1]:
            color = result[1]
            self.display_frame.config(bg=color)
            self.canvas.config(bg=color)
            self.text_frame.config(bg=color)
            self.status.config(
                text="Background color changed to " + color
            )

    def clear(self):
        self.current_image = None
        self.photo = None
        self.current_file = ""

        self.canvas.delete("all")
        self.text_frame.pack_forget()
        self.canvas.pack(fill="both", expand=True)

        self.path_entry.delete(0, tk.END)
        self.text_box.config(state="normal")
        self.text_box.delete("1.0", tk.END)
        self.text_box.config(state="disabled")

        self.info.config(text="No file selected")
        self.status.config(text="Viewer cleared")

    def canvas_click(self, event):
        self.status.config(
            text=f"Canvas clicked at X={event.x}, Y={event.y}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = FileViewer(root)
    root.mainloop()
