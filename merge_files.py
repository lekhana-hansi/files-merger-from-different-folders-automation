import os
from tqdm import tqdm

def merge_files_in_folder(folder_path, output_dir):
    folder_name = os.path.basename(folder_path)
    output_file = os.path.join(output_dir, f"{folder_name}_merged.txt")

    with open(output_file, "w", encoding="utf-8") as outfile:
        files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]

        for file in tqdm(files, desc=f"Merging files in {folder_name}"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
                outfile.write(f"\n--- {file} ---\n")
                outfile.write(infile.read())

    print(f"✅ Merged file created: {output_file}")


def process_all_folders(input_root, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    folders = [
        os.path.join(input_root, d)
        for d in os.listdir(input_root)
        if os.path.isdir(os.path.join(input_root, d))
    ]

    for folder in tqdm(folders, desc="Processing folders"):
        merge_files_in_folder(folder, output_dir)


if __name__ == "__main__":
    INPUT_ROOT = "example_input"
    OUTPUT_DIR = "output"

    process_all_folders(INPUT_ROOT, OUTPUT_DIR)
