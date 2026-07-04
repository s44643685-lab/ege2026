print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = (x or (not z and w) or w) == (y and not x and w)
                if f == True:
                    print(w, x, y, z)

print("Ответ zyxw")