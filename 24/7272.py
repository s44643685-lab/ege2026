with open("7272.txt") as f:
    data = f.readline()

data = data.replace("AB", "*")
data = data.replace("CB", "*")
for i in "ABC":
    data = data.replace(i, "-")
data = data.split("-")
m = max(data, key=len)
print(len(m))