import os

def find_txt_file(filename):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == filename:
                return os.path.relpath(os.path.join(root, file))
    return None

filename_to_search = "Comments.txt"
result = find_txt_file(filename_to_search)

if result:
    comments = result
    print(comments)
else:
    print("File not found.")