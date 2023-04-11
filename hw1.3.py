var_1 = input('Please enter an integer:  ') #string, 4
var_2 = input('Please enter another integer:  ') #string, 5

var_3 = int(var_1) ** int(var_2) #int, 1024
length = len(str(var_3)) #int, 4

print('=' * length)
print(var_3)
print('=' * length)