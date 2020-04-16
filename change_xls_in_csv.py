def xls_in_CSV(file_path):
    file_str = open(file_path, 'r')
    file = file_str.read()
    file_new = file.replace('\t', ';')
    print(file_new)
    name = file_str.name
    len(name)
    new = name.replace('xls', 'csv')
    new_file = open(new, 'w+')
    print(new)
    new_file.write(file_new)
    new_file.close()
    file_str.close()





