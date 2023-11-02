file = open("main2.txt", "r")

for line in file.readlines():
    print(line)

file.close()