# read sums.txt
file = open('sums.txt','r')

for line in file:
    print(sum([int(i) for i in line.split()]))

file.close()

