with open("2410.txt", 'r') as file:
    data = file.readline()




#data = "5183208300000000270062890200298000"
data = data.replace("00", "0*0")
data = data.replace("00", "0*0")
data = data.split("*")
m = max(data, key=len)
print(len(m))