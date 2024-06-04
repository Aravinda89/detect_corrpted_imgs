import os
import argparse
from PIL import Image

def check_and_remove_corrupted_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify the image file integrity
        return False  # Image is not corrupted
    except (IOError, SyntaxError) as e:
        print(f"Removing corrupted image: {file_path} - {e}")
        os.remove(file_path)  # Remove corrupted image file
        return True  # Image was corrupted and removed


def scan_and_clean_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            check_and_remove_corrupted_image(file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan and remove corrupted image files from a dataset.")
    parser.add_argument("./dataset", type=str, help="Path to the dataset directory")
    args = parser.parse_args()

    scan_and_clean_directory(args.directory)
    print("Directory scan and cleanup complete.")
