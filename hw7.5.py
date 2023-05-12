user_input = input('please enter a year:  ')                                                    # str, '1926'

lister = [ i.rstrip() for i in open('FF_tiny.txt') if i.startswith(user_input) ]                # list, ['19270103    0.97    0.21    0.24   0.010', ...]

print(lister)