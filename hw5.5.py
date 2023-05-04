file = open('cities_green_space.csv')                                                       # 'file' object
country_dictionary = {}                                                                     # dict, {}

for line in file:                                                                           # str, 'Amsterdam,13.00%,,2018,Statistics Netherlands/TNO,\n'
    country_info = line.split(',')                                                          # list, ['Amsterdam', '13.00%', ' ', '2018', 'Statistics', 'Netherlands/TNO', '\n']
    country_dictionary[country_info[0]] = round(float(country_info[1].rstrip('%')), 1)      # dict, {'Amsterdam': 13.0}

print('Cities Ranked by Greenspace (% of total area)')
print('')

for country in sorted(country_dictionary, key = country_dictionary.get, reverse = True):    # str, 'Oslo'
    print(f'{country} {country_dictionary[country]}')