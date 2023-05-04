import json

fh = open('config.json')                                # 'file' object
conf = json.load(fh)                                    # list, [{'domain': 'www.example1.com', 'database': ...   ['plugin3', 'eslint-plugin-plugin3']}]

print(conf)

for dictionary in conf:
    print()
    print()
    print(f'domain:  {dictionary["domain"]}')
    print(f'db_host:  {dictionary["database"]["host"]}')
    print(f'db_port:  {dictionary["database"]["port"]}')
    print('plugins:')
    for plugin in dictionary["plugins"]:
        print(f'  {plugin}')

fh.close()