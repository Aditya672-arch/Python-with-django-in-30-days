#Count duplicate data in a tuple
a = (10, 20, 30, 10, 20, 40, 10)

for i in a:
    if a.count(i) > 1:
        print(i, "occurs", a.count(i), "times")