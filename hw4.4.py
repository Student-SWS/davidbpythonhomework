year = '1927'                                           # str, '1927'
mktrf_list = []                                         # list, []
file = open('FF_tiny.txt', 'r')                         # 'file' object

for line in file:                                       # str, '19270103    0.97    0.21    0.24   0.010'
    if line[:4] == '1927':                              # bool, False
        mktrf_list.append(float(line.split()[1]))       # list, [0.97]
    elif int(line[:4]) > int(year):                     # bool, False
        break

print(mktrf_list)
