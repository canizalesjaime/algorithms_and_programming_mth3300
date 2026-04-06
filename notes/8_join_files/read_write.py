persons = {}


with open("file.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(",")
        persons[name]= int(age)+3


with open("file.txt", "w") as file:
    for person in persons:
        file.write(f"{person},{persons[person]}\n")


with open("file.txt", "r") as file:
    for line in file:
        name, age = line.strip().split(",")
        print(name, "is", age, "years old")
        