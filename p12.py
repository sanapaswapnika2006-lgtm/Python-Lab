
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps
import os


class ImageFilterUtility:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Image Filter and Color Converter Utility")
        self.root.geometry("1000x700")
        self.root.configure(bg="#eaf2f8")

        self.original = None
        self.processed = None
        self.photo = None

        tk.Label(
            root,
            text="Digital Image Filter and Color Converter Utility",
            font=("Arial", 18, "bold"),
            bg="#eaf2f8",
            fg="#154360"
        ).pack(pady=15)

        buttons = tk.Frame(root, bg="#eaf2f8")
        buttons.pack(pady=10)

        button_list = [
            ("Open Image", self.open_image),
            ("Grayscale", self.grayscale),
            ("Black & White", self.threshold),
            ("Blur", self.blur),
            ("Reset", self.reset),
            ("Save Image", self.save_image)
        ]

        for i, (text, command) in enumerate(button_list):
            tk.Button(
                buttons,
                text=text,
                command=command,
                width=14,
                font=("Arial", 10, "bold"),
                cursor="hand2"
            ).grid(row=0, column=i, padx=5, pady=5)

        self.preview = tk.Label(
            root,
            text="Click Open Image to select a JPEG or PNG file",
            font=("Arial", 12),
            bg="white",
            relief="sunken"
        )
        self.preview.pack(fill="both", expand=True, padx=20, pady=15)

        self.status = tk.Label(
            root,
            text="Ready - Please open an image",
            bg="#eaf2f8",
            font=("Arial", 10)
        )
        self.status.pack(pady=10)

    def check_image(self):
        if self.original is None:
            messagebox.showwarning(
                "No Image", "Please click Open Image first."
            )
            return False
        return True

    def open_image(self):
        path = filedialog.askopenfilename(
            title="Choose an image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png"),
                ("All files", "*.*")
            ]
        )

        if not path:
            return

        try:
            with Image.open(path) as img:
                self.original = img.convert("RGB")

            self.processed = self.original.copy()
            self.show_image()
            self.status.config(
                text="Loaded: " + os.path.basename(path)
            )

        except Exception as e:
            messagebox.showerror("Open Error", str(e))

    def show_image(self):
        if self.processed is None:
            return

        preview = self.processed.copy()
        preview.thumbnail((900, 480))

        self.photo = ImageTk.PhotoImage(preview)
        self.preview.configure(image=self.photo, text="")

        self.status.config(
            text=f"Image size: {self.processed.width} x "
                 f"{self.processed.height} pixels"
        )

    def grayscale(self):
        if not self.check_image():
            return

        try:
            gray = ImageOps.grayscale(self.original)
            self.processed = gray.convert("RGB")
            self.show_image()
            self.status.config(text="Grayscale filter applied")
        except Exception as e:
            messagebox.showerror("Filter Error", str(e))

    def threshold(self):
        if not self.check_image():
            return

        try:
            gray = ImageOps.grayscale(self.original)

            # Pixels >= 128 become white; others become black.
            binary = gray.point(
                lambda pixel: 255 if pixel >= 128 else 0
            )

            self.processed = binary.convert("RGB")
            self.show_image()
            self.status.config(text="Black and white filter applied")
        except Exception as e:
            messagebox.showerror("Filter Error", str(e))

    def blur(self):
        if not self.check_image():
            return

        try:
            self.processed = self.original.filter(
                ImageFilter.BoxBlur(5)
            )
            self.show_image()
            self.status.config(text="Blur filter applied")
        except Exception as e:
            messagebox.showerror("Filter Error", str(e))

    def reset(self):
        if not self.check_image():
            return

        self.processed = self.original.copy()
        self.show_image()
        self.status.config(text="Original image restored")

    def save_image(self):
        if not self.check_image():
            return

        path = filedialog.asksaveasfilename(
            title="Save processed image",
            defaultextension=".png",
            filetypes=[
                ("PNG image", "*.png"),
                ("JPEG image", "*.jpg *.jpeg")
            ]
        )

        if not path:
            return

        try:
            image_to_save = self.processed

            if path.lower().endswith((".jpg", ".jpeg")):
                image_to_save = self.processed.convert("RGB")

            image_to_save.save(path)
            self.status.config(text="Saved: " + os.path.basename(path))
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Save Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterUtility(root)
    root.mainloop()
