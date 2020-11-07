# write your code here

for file in range(1, 11):
    with open('file{}.txt'.format(file), 'w') as f:
        f.write(str(file))
