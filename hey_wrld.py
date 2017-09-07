lst = [1, 1, 1, 3, 2, 5, 3, 5, 9, 9, 9, 8]

for item in lst:
    if item == 9:
        lst.remove(item)

print(lst)