for row in range(9, -1, -1):
    start = row * 10 + 1

    if row % 2 == 0:
        for i in range(start, start + 10):
            print(i, end=" ")
    else:
        for i in range(start + 9, start - 1, -1):
            print(i, end=" ")

    print() 