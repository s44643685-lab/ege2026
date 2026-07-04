with open("2416.txt", 'r') as file:
    data = file.readline()
for i in ["AB", "AD", "AC", "EB", "EC", "ED"]:
    data = data.replace(i, "*")
for i in "ABCED":
    data = data.replace(i, "-")

data = data.split("-")
m = max(data, key=len)
print(len(m))

