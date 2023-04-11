while True:                                             # bool, True
    year = input("please enter a 4-digit year: ")       # str, '1983'

    if len(year) == 4 and year.isdigit():               # bool, True
        print(f'thanks! Your value is {year}')
        break

    else:                                               # bool, False
        print('sorry, that was bad input')