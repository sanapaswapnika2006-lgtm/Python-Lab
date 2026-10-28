
import pickle
import shelve
import os


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)


class PersistenceEngine:
    @staticmethod
    def save_pickle(student):
        try:
            with open("student.pkl", "wb") as file:
                pickle.dump(student, file)
            print("Student saved successfully using Pickle!")
        except (OSError, pickle.PickleError) as error:
            print("Save error:", error)

    @staticmethod
    def load_pickle():
        try:
            with open("student.pkl", "rb") as file:
                student = pickle.load(file)
            print("Student loaded successfully using Pickle!")
            return student
        except FileNotFoundError:
            print("No saved Pickle file found.")
        except (OSError, pickle.PickleError, EOFError, AttributeError,
                ImportError, ModuleNotFoundError) as error:
            print("Load error:", error)
        return None

    @staticmethod
    def save_shelve(student):
        try:
            with shelve.open("student_db") as database:
                database["student"] = student
            print("Student saved successfully using Shelve!")
        except (OSError, pickle.PickleError) as error:
            print("Save error:", error)

    @staticmethod
    def load_shelve():
        try:
            with shelve.open("student_db") as database:
                student = database.get("student")

            if student is None:
                print("No saved student found in Shelve.")
                return None

            print("Student loaded successfully using Shelve!")
            return student
        except (OSError, pickle.PickleError, EOFError, AttributeError,
                ImportError, ModuleNotFoundError) as error:
            print("Load error:", error)
        return None


def main():
    engine = PersistenceEngine()
    student = None

    while True:
        print("\n===== OBJECT PERSISTENCE ENGINE =====")
        print("1. Create Student")
        print("2. Save using Pickle")
        print("3. Load using Pickle")
        print("4. Save using Shelve")
        print("5. Load using Shelve")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                roll_no = int(input("Enter roll number: "))
                name = input("Enter student name: ").strip()
                marks = float(input("Enter marks: "))

                student = Student(roll_no, name, marks)
                print("\nStudent created successfully!")
                student.display()

            except ValueError:
                print("Invalid input! Enter numeric roll number and marks.")

        elif choice == "2":
            if student is not None:
                engine.save_pickle(student)
            else:
                print("Create or load a student first.")

        elif choice == "3":
            loaded = engine.load_pickle()
            if loaded is not None:
                student = loaded
                student.display()

        elif choice == "4":
            if student is not None:
                engine.save_shelve(student)
            else:
                print("Create or load a student first.")

        elif choice == "5":
            loaded = engine.load_shelve()
            if loaded is not None:
                student = loaded
                student.display()

        elif choice == "6":
            print("Program terminated.")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
