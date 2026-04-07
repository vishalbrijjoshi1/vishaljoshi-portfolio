#This script will read a text file and count its character, 
# words, and count lines, After that create a small report.
def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Count lines of content using splitlines function and store in lines, 
        # using len() find the length of lines and store in line_count 
        lines = content.splitlines()
        line_count = len(lines)

        # Count words using split() function and find the length using len() fuction
        words = content.split()
        word_count = len(words)

        # Count characters (including spaces)
        char_count = len(content)

        # Print report
        print("----- File Analysis Report -----")
        print(f"File Name      : {file_path}")
        print(f"Total Lines    : {line_count}")
        print(f"Total Words    : {word_count}")
        print(f"Total Characters: {char_count}")
        print("--------------------------------")

    except FileNotFoundError: #Error handling 
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage Define the analyze_file fuction and define the filepath after defining the fuction first
file_path = "test_script1.txt"  # Replace with your file name
analyze_file(file_path)