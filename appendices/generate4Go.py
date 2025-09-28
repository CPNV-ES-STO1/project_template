import os
import random
import string
from pathlib import Path

# Root folder for test data
ROOT_DIR = Path("test_data")
TARGET_SIZE = 4 * 1024 * 1024 * 1024  # ~4 GB

# File extensions (mix of text, binary, media, compressed)
FILE_TYPES = [
    ".txt", ".docx", ".pdf", ".csv", ".json",
    ".jpg", ".png", ".mp4", ".mov", ".zip"
]

# Max folder depth
MAX_DEPTH = 5

# To track total size created
total_size = 0


def random_string(length=12):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def make_random_file(path: Path, extension: str, size: int):
    """Create a random file of given size in bytes."""
    with open(path.with_suffix(extension), "wb") as f:
        f.write(os.urandom(size))


def create_folder_tree(base: Path, depth=0):
    global total_size

    if total_size >= TARGET_SIZE:
        return

    # Decide how many subfolders and files
    num_subfolders = random.randint(1, 4) if depth < MAX_DEPTH else 0
    num_files = random.randint(2, 6)

    # Create files in this folder
    for _ in range(num_files):
        if total_size >= TARGET_SIZE:
            return

        filename = random_string()
        extension = random.choice(FILE_TYPES)

        # Decide file size depending on type
        if extension in [".mp4", ".mov"]:
            size = random.randint(50 * 1024 * 1024, 500 * 1024 * 1024)  # 50MB–500MB
        elif extension in [".jpg", ".png"]:
            size = random.randint(100 * 1024, 5 * 1024 * 1024)  # 100KB–5MB
        elif extension in [".zip"]:
            size = random.randint(5 * 1024 * 1024, 50 * 1024 * 1024)  # 5MB–50MB
        else:
            size = random.randint(1 * 1024, 1 * 1024 * 1024)  # 1KB–1MB

        filepath = base / filename
        make_random_file(filepath, extension, size)

        total_size += size
        print(f"Created {filepath}{extension} ({size/1024/1024:.2f} MB)")

    # Create subfolders recursively
    for _ in range(num_subfolders):
        if total_size >= TARGET_SIZE:
            return

        subfolder = base / random_string(8)
        subfolder.mkdir(parents=True, exist_ok=True)
        create_folder_tree(subfolder, depth + 1)


if __name__ == "__main__":
    ROOT_DIR.mkdir(exist_ok=True)
    create_folder_tree(ROOT_DIR)
    print(f"\nDone. Total size generated: {total_size/1024/1024/1024:.2f} GB")
