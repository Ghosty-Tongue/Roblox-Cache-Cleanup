import os
import math

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
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file: {file_path}, Error: {e}")

if __name__ == "__main__":
    directory_to_clean = os.path.expanduser("~/AppData/Local/Temp/Roblox")
    if os.path.exists(directory_to_clean):
        directory_size = get_directory_size(directory_to_clean)
        print(f"Size of directory '{directory_to_clean}': {directory_size}")

        if directory_size != "0B":
            delete_files_in_directory(directory_to_clean)
            print("All files deleted successfully.")
        else:
            print("You have already cleaned out the Roblox caches. Thank you for using the script.")
    else:
        print("Directory does not exist.")

    input("Press Enter to exit...")
