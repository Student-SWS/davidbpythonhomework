p1size = input('please enter the unit size of Product 1: ') #string, 500
p1price = input('please enter the price of Product 1: ') #string, 20
p2size = input('please enter the unit size of Product 2: ') #string, 800
p2price = input('please enter the price of Product 2: ') #string, 25

p1costper = float(p1price)/float(p1size) #float, 0.04
p2costper = float(p2price)/float(p2size) #float, 0.03125
p1p2ratiopercent = p1costper/p2costper*100 #float, 128

print('Product 1 costs $' + str(p1costper) + ' per unit')
print('Product 2 costs $' + str(p2costper) + ' per unit')
print('Product 1 is ' + str(p1p2ratiopercent) + '% the per unit cost of Product 2')