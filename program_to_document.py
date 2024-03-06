import sys

try:
    file_name = input("Enter filename: ")
    file = open(file_name, "w")
except IOError:
    print("There was an error writing to", file_name)
    sys.exit()

file_finish = "done"
print("Enter '", file_finish, "' when finished")

while True:
    file_text = input("Enter text: ")
    if file_text == file_finish:
        file.close()
        break
    file.write(file_text + "\n")

file.close()
print("File written successfully.")
