with open("13866.txt") as file:
    data = file.readline()

data = data.replace("1", ".")
data = data.replace("3", ".")
data = data.replace("5", ".")
data = data.replace("7", ".")
data = data.replace("9", ".")
while "..." in data:
    data = data.replace("...", ".*.*.")
data = data.split("*")

m = max(data, key=len)
print(len(m))
