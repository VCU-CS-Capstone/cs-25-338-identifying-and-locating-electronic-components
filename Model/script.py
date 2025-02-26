import os
import shutil
import random

def move_every_nth_file(source_dir, destination_dir, n=4):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of all files in the source directory
    files = sorted(os.listdir(source_dir))

    # Move every nth file
    for i, file in enumerate(files):
        if (i + 1) % n == 0:  # Check if the file is the nth file
            source_path = os.path.join(source_dir, file)
            destination_path = os.path.join(destination_dir, file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {file}")

def shuffle_images_and_labels(images_dir, labels_dir):
    images = sorted(os.listdir(images_dir))
    labels = sorted(os.listdir(labels_dir))

    # Ensure the number of images and labels are the same
    assert len(images) == len(labels), "The number of images and labels must be the same."

    combined = list(zip(images, labels))
    random.shuffle(combined)

    for i, (image, label) in enumerate(combined):
        new_image_name = f"{i:04d}_{image}"
        new_label_name = f"{i:04d}_{label}"

        os.rename(os.path.join(images_dir, image), os.path.join(images_dir, new_image_name))
        os.rename(os.path.join(labels_dir, label), os.path.join(labels_dir, new_label_name))

if __name__ == "__main__":
    move_every_nth_file("images/train", "images/val", n=4)
    move_every_nth_file("labels/train", "labels/val", n=4)
    shuffle_images_and_labels("images/val", "labels/val")