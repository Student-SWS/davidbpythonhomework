try:
    int1 = int(input('please enter an int: '))                          # int, 8
    int2 = int(input('please enter an int: '))                          # int, 3
    quotient = round(int1/int2, 2)                                      # float, 2.67
except ZeroDivisionError:
    print('error:  second value cannot be zero')
    quit()
except ValueError:
    print('error:  both values must be whole numbers')
    quit()

print(f'{int1} / {int2} = {quotient}')