with open("2417.txt", 'r') as file:
    data = file.readline()

data = data.replace("Q", ".")
data = data.replace("S", ".")
data = data.replace("R", ".")
while ".." in data:
    data = data.replace ("..", ".*.")
data = data.split("*")

m = max(data, key=len)
print(len(m))
