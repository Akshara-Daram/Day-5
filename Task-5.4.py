import os

def organize_files(directory):
  file_types = {
    "image": "Images",
    "document": "Documents",
    "video": "Videos",
    "other": "Others"
  }
  for file_type in file_types.values():
    os.makedirs(os.path.join(directory, file_type), exist_ok=True)

  for file in os.listdir(directory):

    file_type = os.path.splitext(file)[1]

    if file_type not in file_types:
      file_type = "other"

    os.rename(os.path.join(directory, file), os.path.join(directory, file_types[file_type], file))


if __name__ == "__main__":
  directory = input("Choose a directory to organize: ")
  organize_files(directory)

  print("Files organized into subdirectories:")
  for file_type in file_types.values():
    print(f"- {file_type}")
