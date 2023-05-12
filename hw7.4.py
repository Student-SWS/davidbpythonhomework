def get_student_name(stuid):
    file = open('student_db_names.txt')                         # 'file' object
    for line in file:                                           # str, 'id:fname:lname:address:city:state:zip'
        line_list = line.split(':')                             # list, ['id', 'fname', 'lname', 'address', 'city', 'state', 'zip']
        if line_list[0] == stuid:                               # bool, False
            name = f'{line_list[1]} {line_list[2]}'            # str, 'fname lname'
            return name

sid = 'ap172'                                                   # str, 'ap172'
name = get_student_name(sid)                                    # str, 'Anton Perillo'
print(name)

sid = 'jab44'                                                   # str, 'jab44'
name = get_student_name(sid)                                    # str, 'Janine Brillo'
print(name)

sid = 'xxx'                                                     # str, 'xxx'
name = get_student_name(sid)                                    # None
print(name)