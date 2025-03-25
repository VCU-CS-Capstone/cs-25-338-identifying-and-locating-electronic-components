import os
import shutil

def move_every_4th_file(source_folder, target_folder):
    """Move every 4th file from source_folder to target_folder."""
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    files = sorted(os.listdir(source_folder))  # Sort files for consistency
    moved_files = 0

    for index, file in enumerate(files, start=1):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path) and index % 4 == 0:
            shutil.move(file_path, os.path.join(target_folder, file))
            moved_files += 1
            print(f"Moved: {file}")

    print(f"Total files moved: {moved_files}")

if __name__ == "__main__":
    source_folder = "./labels/train"
    target_folder = "./labels/val"

    if os.path.isdir(source_folder):
        move_every_4th_file(source_folder, target_folder)
    else:
        print("Invalid source folder path.")
