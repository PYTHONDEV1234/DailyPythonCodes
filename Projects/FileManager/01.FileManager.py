import os

def list_files_and_folders(directory):
    """
    Lists all files and folders in the specified directory.
    """
    print(f"Contents of directory: {directory}")
    print("-" * 30)
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            print(f"Folder: {item}")
        else:
            print(f"File: {item}")
    print("-" * 30)

def view_file_contents(directory, filename):
    """
    Views the contents of a specified file.
    """
    file_path = os.path.join(directory, filename)
    # C:\Users\HP\Desktop\Academy\NEWWEB
    # index.js
    # file_path = C:\Users\HP\Desktop\Academy\NEWWEB\index.js
    print(f"Contents of file: {filename}")
    print("-" * 30)
    try:
        with open(file_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    print("-" * 30)

def delete_file_or_folder(directory, name):
    """
    Deletes a specified file or folder.
    """
    item_path = os.path.join(directory, name)
    try:
        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Deleted file: {name}")
        elif os.path.isdir(item_path):
            os.rmdir(item_path)
            print(f"Deleted folder: {name}")
        else:
            print(f"Error: '{name}' is neither a file nor a folder.")
    except OSError as e:
        print(f"Error: {e}")

def create_file(directory, filename):
    """
    Creates a new file in the specified directory.
    """
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'w') as file:
            print(f"Created file: {filename}")
    except OSError as e:
        print(f"Error: {e}")

def create_folder(directory, foldername):
    """
    Creates a new folder in the specified directory.
    """
    folder_path = os.path.join(directory, foldername)
    try:
        os.mkdir(folder_path)
        print(f"Created folder: {foldername}")
    except OSError as e:
        print(f"Error: {e}")

def rename_file_or_folder(directory, old_name, new_name):
    """
    Renames a specified file or folder.
    """
    old_path = os.path.join(directory, old_name)
    new_path = os.path.join(directory, new_name)
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    except OSError as e:
        print(f"Error: {e}")

def main():
    """
    Main function to interact with the file manager.
    """
    directory = input("Enter directory path: ").strip()

    while True:
        print("\nFile Manager Menu:")
        print("1. List files and folders")
        print("2. View file contents")
        print("3. Delete file or folder")
        print("4. Create file")
        print("5. Create folder")
        print("6. Rename file or folder")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            list_files_and_folders(directory)
        elif choice == '2':
            filename = input("Enter filename to view contents: ").strip()
            view_file_contents(directory, filename)
        elif choice == '3':
            name = input("Enter name of file or folder to delete: ").strip()
            delete_file_or_folder(directory, name)
        elif choice == '4':
            filename = input("Enter filename to create: ").strip()
            create_file(directory, filename)
        elif choice == '5':
            foldername = input("Enter folder name to create: ").strip()
            create_folder(directory, foldername)
        elif choice == '6':
            old_name = input("Enter current name of file or folder: ").strip()
            new_name = input("Enter new name: ").strip()
            rename_file_or_folder(directory, old_name, new_name)
        elif choice == '7':
            print("Exiting File Manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()


# Tasks for Ansel - Read About OS module - w3schools 
# Try few more functions from OS module 
# Modularise the code 
