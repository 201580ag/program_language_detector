import os
from pygments.lexers import get_lexer_for_filename

def detect_programming_language(filename):
    try:
        lexer = get_lexer_for_filename(filename)
        language = lexer.name
        return language
    except:
        return "Unknown"

def explore_folder(folder_path):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            language = detect_programming_language(file_path)
            result = f"{file} - {language}"
            results.append(result)
            print(result)

    with open("result.txt", "w") as file:
        file.write(f"Results for folder : {folder_path}\n\n")
        for result in results:
            file.write(result + "\n")

folder_path = input(r"Please enter the folder path where the files are located : ")

explore_folder(folder_path)

print("\n\n\n" + "It is saved to the result.txt file.")