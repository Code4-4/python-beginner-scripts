# file_backup.py
import shutil
import os

def backup_file(file_path):
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return
    
    backup_path = file_path + ".bak"
    shutil.copy(file_path, backup_path)
    print(f"Backup created at {backup_path}")

if __name__ == "__main__":
    file = input("Enter the path of the file to back up: ")
    backup_file(file)
