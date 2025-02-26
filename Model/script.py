import os
import re

def restore_original_filenames(directory):
    for file in os.listdir(directory):
        # Remove the "XXXX_" prefix from filenames
        new_name = re.sub(r'^\d{4}_', '', file)
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_name)

        if old_path != new_path:  # Avoid renaming if the name is unchanged
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")

if __name__ == "__main__":
    restore_original_filenames("images/val")
    restore_original_filenames("labels/val")
