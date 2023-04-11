year = '1927'                               # str, '1926'
total = 0.0                                 # float, 0.0
counter = 0                                 # int, 0

file = open("FF_data.txt", "r")             # 'file' object

for line in file:                           # str, '19260701    0.09   -0.22   -0.30   0.009'

    if line[:4] == year:                    # bool, False
        split_line = line.split()           # list, [19260701, 0.09, -0.22, -0.30, 0.009]
        counter += 1                        # int, 1
        total += float(split_line[1])       # float, 0.09

    elif float(line[0:4]) >= float(year):   # bool, False
        break

print(counter)
print(round(total, 2))