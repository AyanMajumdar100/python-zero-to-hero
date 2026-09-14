# # FILES
# Python can open a file, read its contents, and then close the file when finished.
# The preferred modern pattern is the with open(...) context manager because it automatically closes the file even if an error occurs.
# When working with text, you should normally specify an encoding such as UTF-8.
# You should know the difference between reading the entire file and reading it line by line.
# Reading line by line is more memory-efficient for very large files.
# In our RAG project, reading files will form the foundation for loading text, prompt templates, 
# evaluation datasets, configuration files, and extracted document content.

# EXMAPLE 1 : read() 
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
# "r" means read mode.
# encoding="utf-8" ensures Python correctly interprets modern text.
# The with block closes the file automatically after reading.

# EXAMPLE 2 : readlines() : Returning a list of lines in the file
with open("notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
# readlines() returns a list containing the lines of the file.
# strip() removes surrounding whitespace such as the newline character.


# For very large files, you can avoid loading every line at once by iterating directly over the file.
total_words = 0
with open("large_text.txt", "r", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        total_words += len(words)
print("Total words:", total_words)


# WRITE MODE : "w" - > creates new file if not present
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python\n")
    file.write("This is a new file.\n")

# REWRITES THE FILE 
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Java\n")

# APPENDING AT THE END OF THE FILE -> "a"
with open("output.txt", "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")