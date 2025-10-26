n = 5
rows = 3
for i in range(rows):
    for j in range(1, n * rows + 1):
        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 0):
            print('*', end='')
        else:
            print(' ', end='')
    print()
