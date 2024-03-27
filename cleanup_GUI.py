# Don't use it waste more time please use cleanup,py without the GUI

import os
import math
import tkinter as tk
from tkinter import messagebox

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return convert_size(total_size)

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def delete_files_in_directory(directory):
    deleted_files = []
    failed_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
            except Exception as e:
                failed_files.append((file_path, e))
    return deleted_files, failed_files

def clean_directory():
    directory_to_clean = os.path.expanduser("~/AppData/Local/Temp/Roblox")
    if os.path.exists(directory_to_clean):
        directory_size = get_directory_size(directory_to_clean)
        result = messagebox.askokcancel("Confirmation", f"Do you want to delete {directory_size} of files?")
        if result:
            deleted_files, failed_files = delete_files_in_directory(directory_to_clean)
            show_logs(deleted_files, failed_files)
        else:
            messagebox.showinfo("Info", "Operation cancelled by user.")
    else:
        messagebox.showerror("Error", "Directory does not exist.")

def show_logs(deleted_files, failed_files):
    log_window = tk.Toplevel()
    log_window.title("Deletion Logs")

    log_text = tk.Text(log_window, wrap="word")
    log_text.pack(fill="both", expand=True)

    log_text.insert("end", "Deleted Files:\n")
    for file_path in deleted_files:
        log_text.insert("end", f"{file_path}\n")

    log_text.insert("end", "\nFailed Files:\n")
    for file_path, error in failed_files:
        log_text.insert("end", f"{file_path}: {error}\n")

root = tk.Tk()
root.title("Roblox Cache Cleaner")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

button = tk.Button(frame, text="Clean Cache", command=clean_directory)
button.pack()

root.mainloop()
