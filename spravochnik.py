def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

readall('Data_txt')