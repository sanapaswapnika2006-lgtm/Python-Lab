
import os
import sys

def main():
    # 1. Display the current directory
    current_dir = os.getcwd()
    print("Current Directory:", current_dir)

    # 2. List files and directories
    print("\nFiles and Directories:")
    for item in os.listdir(current_dir):
        print(item)

    # 3. Navigate to a directory given as an argument
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]

        if os.path.isdir(target_dir):
            os.chdir(target_dir)
            print("\nChanged Directory:", os.getcwd())
        else:
            print("\nDirectory does not exist:", target_dir)

    # 4. Create a workspace directory
    workspace = "workspace"
    os.makedirs(workspace, exist_ok=True)
    print("\nWorkspace created/available:", workspace)

    # 5. List files with a specific extension
    extension = ".txt"
    print("\nText Files:")
    for item in os.listdir("."):
        if os.path.isfile(item) and os.path.splitext(item)[1] == extension:
            print(item)

    # 6. Safely read or create a log file
    log_file = "activity.log"

    try:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write("File utility executed successfully.\n")

        with open(log_file, "r", encoding="utf-8") as file:
            print("\nLog Contents:")
            print(file.read())

    except OSError as error:
        print("File operation failed:", error)


if __name__ == "__main__":
    main()
