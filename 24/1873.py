with open("1873.txt", 'r') as file:
    data = file.readline()

data = data.replace("RP", "R*P")
data = data.replace("PR", "P*R")
data = data.split("*")
m = max(data, key=len)
print(len(m))