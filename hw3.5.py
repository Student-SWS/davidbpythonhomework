while True:                                             # bool, True
    year = input("please enter a 4-digit year: ")       # str, '1927'

    if len(year) == 4 and year.isdigit():               # bool, True
        break

    else:                                               # bool, False
        print('sorry, that was bad input')

total = 0.0                                             # float, 0.0
counter = 0                                             # int, 0
file = open("FF_data.txt", "r")                         # 'file' object

for line in file:                                       # str, '19260701    0.09   -0.22   -0.30   0.009'

    if line[:4] == year:                                # bool, False
        split_line = line.split()                       # list, [19260701, 0.09, -0.22, -0.30, 0.009]
        counter += 1                                    # int, 1
        total += float(split_line[1])                   # float, 0.09

    elif float(line[0:4]) >= float(year):               # bool, False
        break

average = round(total/counter, 2)                       # float, 0.11

print(f'count {counter}, sum {round(total, 2)}, avg {average}')

exit()