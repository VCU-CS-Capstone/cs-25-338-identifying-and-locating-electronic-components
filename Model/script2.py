import os

def count_files_in_folders(directory):
    folder_counts = {}
    
    for foldername, _, filenames in os.walk(directory):
        folder_counts[foldername] = len(filenames)
    
    return folder_counts

if __name__ == "__main__":
    directory = "./labels"
    file_counts = count_files_in_folders(directory)
    
    for folder, count in file_counts.items():
        print(f"{folder}: {count} files")
