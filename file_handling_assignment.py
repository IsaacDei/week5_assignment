# file_handling_assignment.py

def create_file():
    """Creates a new file and writes initial content to it."""
    try:
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line.\n")
            file.write("Here is the second line.\n")
            file.write("And the third line with a number: 12345.\n")
        print("File created and initial content written.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating or writing to the file: {e}")

def read_file():
    """Reads the contents of the file and displays them on the console."""
    try:
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nFile content after initial write:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while reading the file: {e}")

def append_to_file():
    """Appends additional content to the file."""
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending the fourth line.\n")
            file.write("Here's the fifth line.\n")
            file.write("And the sixth line with more text.\n")
        print("\nAdditional content appended to the file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to the file: {e}")

def main():
    """Main function to perform file handling tasks."""
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to show the appended content

if __name__ == "__main__":
    main()
