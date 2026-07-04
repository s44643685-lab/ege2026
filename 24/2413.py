with open("2413.txt") as f:
    data = f.readline()
# data = "672816625"
l = 0
m = 0
for r in range(len(data) - 2):
    print(data[r], data[r + 1])
    if int(data[r]) < int(data[r + 1]):
        l = r + 1
    length = r - l + 2
    m = max(m, length)
print(m)
