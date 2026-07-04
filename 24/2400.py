with open("2400.txt") as f:
    data = f.readline()

data = data.replace("NPO", "*")
data = data.replace("PNO", "*")
for i in "PNO":
    data = data.replace(i, "-")
data = data.split("-")
m = max(data, key=len)
print(len(m))



