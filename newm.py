my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
while my_list[start] >= 0 and len(my_list) > start:
    if my_list[start] == 0:
        start += 1
    print(my_list[start])
    start += 1
