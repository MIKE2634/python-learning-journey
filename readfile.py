with open("students.txt", "w") as file:
    file.write("Mike"
               "animals"
               "cows"
               "swert")

with open("students.txt", "r") as file:
    data = file.read()
    print(data)
with open("students.txt") as file:
    data = file.del()
    print(data)
