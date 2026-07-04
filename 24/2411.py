with open("2411.txt", 'r') as file:
    data = file.readline()

data = data.replace("12", "1*2")
data = data.replace("21", "2*1")
data = data.replace("13", "1*3")
data = data.replace("31", "3*1")
data = data.split("*")
m = max(data, key=len)
print(len(m))