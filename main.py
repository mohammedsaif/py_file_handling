file = open("students.txt", "w")

file.write("Name: Saif\n")
file.write("Course: Python\n")

file.close()

print("Student details saved successfully!")



file = open("students.txt", "r")

content = file.read()

print(content)

file.close()


with open("students.txt", "r") as file:
    print(file.readline(), end="")
    print(file.readline(), end="")


file = open("students.txt", "a")

file.write("Name: Ahmed\n")
file.write("Course: Data Science\n")

file.close()

print("New student added successfully!")




try:
    with open("unknown.txt","r") as file:
     content = file.read()
     print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Permission denied")
except OSError:
    print("OS Err")
finally:
   print("code execution done")





