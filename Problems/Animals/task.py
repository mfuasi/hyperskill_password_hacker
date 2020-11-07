# read animals.txt
# and write animals_new.txt
output = open('animals.txt', 'r')
to_write = ''.join(output.readlines()).replace('\n', ' ')
output.close()

file = open('animals_new.txt', 'a')
file.write(to_write)
file.close()
