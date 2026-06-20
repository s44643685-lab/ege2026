with open("2401.txt", 'r') as file:
    data = file.readline()




#data = "ABCAABACACAB"
data = data.replace("ad", "a*d")
data = data.replace("da", "d*a")
data = data.split("*")

'''
m = len(data[0])
for i in data:
    if len(i) > m:
        m = len(i)
print(m)
'''
m = max(data,key=len)
print(len(m))