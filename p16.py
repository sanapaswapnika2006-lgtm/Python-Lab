
import traceback
import logging
import os


# Configure error logging
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Custom exception hierarchy
class FileProcessorError(Exception):
    """Base exception for file processing errors."""
    pass


class InvalidFileFormatError(FileProcessorError):
    """Raised when a file contains invalid data."""
    pass


class EmptyFileError(FileProcessorError):
    """Raised when the input file is empty."""
    pass


# File processing class
class SafeFileProcessor:

    def process_file(self, filename):
        file = None

        try:
            file = open(filename, "r", encoding="utf-8")
            print("\nFile opened successfully.")

            content = file.read()

            if not content.strip():
                raise EmptyFileError("The file is empty.")

            lines = content.splitlines()

            # Expected format: name,age
            for line_number, line in enumerate(lines, start=1):
                parts = line.split(",")

                if len(parts) != 2:
                    raise InvalidFileFormatError(
                        f"Invalid format on line {line_number}: {line}"
                    )

                name = parts[0].strip()
                age_text = parts[1].strip()

                if not name:
                    raise InvalidFileFormatError(
                        f"Name is missing on line {line_number}."
                    )

                try:
                    age = int(age_text)
                except ValueError:
                    raise InvalidFileFormatError(
                        f"Age must be an integer on line {line_number}."
                    )

                if age < 0:
                    raise InvalidFileFormatError(
                        f"Age cannot be negative on line {line_number}."
                    )

            print("\nFile processed successfully!")
            print("Student records:")

            for line in lines:
                name, age = line.split(",")
                print("Name:", name.strip(), "| Age:", int(age.strip()))

        except FileNotFoundError:
            print("Error: File not found.")
            logging.error("File not found: %s", filename)
            logging.error(traceback.format_exc())

        except PermissionError:
            print("Error: Permission denied.")
            logging.error("Permission denied: %s", filename)
            logging.error(traceback.format_exc())

        except FileProcessorError as error:
            print("Processing Error:", error)
            logging.error("File processing failed: %s", error)
            logging.error(traceback.format_exc())

        except OSError as error:
            print("File system error:", error)
            logging.error("File system error: %s", error)
            logging.error(traceback.format_exc())

        except Exception as error:
            print("Unexpected error:", error)
            logging.error("Unexpected error: %s", error)
            logging.error(traceback.format_exc())

        else:
            print("No errors occurred during processing.")

        finally:
            if file is not None and not file.closed:
                file.close()
                print("\nFile closed safely.")
            else:
                print("\nNo open file needs closing.")


def create_sample_file():
    filename = "students.txt"

    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Rahul,20\n")
            file.write("Priya,21\n")
            file.write("Amit,19\n")

    return filename


def main():
    processor = SafeFileProcessor()

    print("===== SAFE FILE PROCESSOR =====")
    print("1. Process sample file")
    print("2. Process another file")
    print("3. Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            filename = create_sample_file()
            processor.process_file(filename)

        elif choice == "2":
            filename = input("Enter file name or path: ").strip()
            processor.process_file(filename)

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
