def custom_write(file_name,string):
    strings_positions={}
    n=0
    for line in string:
        with open(file_name, "a+" ,encoding= "utf-8")as number: #а+ открытие и дозапись
            p=number.tell()
            number.write(line+"\n")
        n+=1
        strings_positions.update({(n,p):line})
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
