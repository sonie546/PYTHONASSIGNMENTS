input_path = "c:\\Users\\ADMIN\\OneDrive - thumbi74\\Desktop\\PYTHON\\output.txt"   # Input file
output_path = "c:\\Users\\ADMIN\\OneDrive - thumbi74\\Desktop\\PYTHON\\outpt.txt"  # Output file

try:
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
        upper_content = content.upper()
        word_count = len(content.split())

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write("PROCESSED TEXT:\n")
        outfile.write(upper_content + "\n\n")
        outfile.write(f"WORD COUNT: {word_count}")

    print("Processed content and word count written to output.txt")

except FileNotFoundError:
    print(f"The file {input_path} does not exist.")


    # Task: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
    filename = input("Enter the filename you want to read: ")

try:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\nFile content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")