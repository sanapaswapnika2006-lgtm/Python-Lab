
import tkinter as tk
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Functional Desktop Calculator")
        self.root.geometry("380x520")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        # Display
        self.display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.GROOVE,
            state="readonly"
        )
        self.display.grid(
            row=0, column=0, columnspan=4,
            padx=10, pady=15, sticky="nsew"
        )

        # Button layout
        buttons = [
            ("C", 1, 0), ("⌫", 1, 1), ("(", 1, 2), (")", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("%", 5, 2), ("+", 5, 3),
            ("√", 6, 0), ("x²", 6, 1), ("1/x", 6, 2), ("=", 6, 3)
        ]

        for text, row, col in buttons:
            button = tk.Button(
                root,
                text=text,
                font=("Arial", 16, "bold"),
                command=lambda value=text: self.click(value),
                bg="#e6e6e6" if text not in ("=", "C") else
                   "#4CAF50" if text == "=" else "#ff9999",
                activebackground="#cccccc"
            )
            button.grid(
                row=row, column=col,
                padx=4, pady=4, sticky="nsew",
                ipadx=4, ipady=10
            )

        # Make grid cells expand evenly
        for col in range(4):
            self.root.grid_columnconfigure(col, weight=1)

        for row in range(7):
            self.root.grid_rowconfigure(row, weight=1)

        # Keyboard support
        self.root.bind("<Key>", self.keyboard_input)

    def update_display(self):
        self.display_var.set(self.expression if self.expression else "0")

    def click(self, value):
        if value == "C":
            self.expression = ""
            self.update_display()

        elif value == "⌫":
            self.expression = self.expression[:-1]
            self.update_display()

        elif value == "=":
            self.calculate()

        elif value in ("√", "x²", "1/x"):
            self.apply_function(value)

        else:
            if self.expression == "Error":
                self.expression = ""

            if value == "%":
                self.expression += "/100"
            else:
                self.expression += value

            self.update_display()

    def apply_function(self, function):
        try:
            if not self.expression:
                return

            number = self.safe_evaluate(self.expression)

            if function == "√":
                if number < 0:
                    raise ValueError("Square root of a negative number")
                result = math.sqrt(number)

            elif function == "x²":
                result = number ** 2

            else:
                if number == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = 1 / number

            self.expression = self.format_result(result)
            self.update_display()

        except Exception:
            self.expression = "Error"
            self.update_display()

    def calculate(self):
        try:
            if not self.expression:
                return

            result = self.safe_evaluate(self.expression)
            self.expression = self.format_result(result)
            self.update_display()

        except Exception:
            self.expression = "Error"
            self.update_display()

    @staticmethod
    def safe_evaluate(expression):
        # Allow only arithmetic expressions, not arbitrary Python code.
        allowed = set("0123456789.+-*/() ")
        if not all(char in allowed for char in expression):
            raise ValueError("Invalid expression")

        result = eval(expression, {"__builtins__": {}}, {})

        if not isinstance(result, (int, float)) or not math.isfinite(result):
            raise ValueError("Invalid result")

        return result

    @staticmethod
    def format_result(result):
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(round(result, 10))

    def keyboard_input(self, event):
        if event.char in "0123456789.+-*/()":
            self.click(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "BackSpace":
            self.click("⌫")
        elif event.keysym == "Escape":
            self.click("C")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
