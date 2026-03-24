# file = open("example.txt", "w")
# file.write("Hello, world!")
# file.close()

with open("example.txt", "w") as file:
    file.write("Hello,\n world")


# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())

with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)