import os
import shutil

def move_every_nth_image(source_dir, destination_dir, n=4):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of all files in the source directory
    files = sorted([f for f in os.listdir(source_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt'))])

    # Move every nth image
    for i, file in enumerate(files):
        if (i + 1) % n == 0:  # Check if the file is the nth image
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            shutil.copy(source_path, destination_path)
            print(f"Moved: {file}")

if __name__ == "__main__":
    move_every_nth_image("labels/train", "labels/val", n=4)