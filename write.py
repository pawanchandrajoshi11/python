with open('files/write.txt', 'w') as write_file:
    write_file.write('Lorem Ispum, python is awesome')

with open('files/write.txt', 'a') as write_file:
    write_file.write('\n I am hero')


# w = write to a file
# a = ammend a file, doesn't delete previous data 

quotes = [
    '\n asdada',
    '\n asdewr',
    '\n otrgrt'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)