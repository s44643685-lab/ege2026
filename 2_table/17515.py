print("w x y z")
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(x <= w) or (y <= z) or not y
                if f == False:
                    print(w, x, y, z)
print("Ответ yxwz")