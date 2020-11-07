# write your code here

with open('salary.txt', 'r') as f1:
    with open('salary_year.txt', 'w', encoding='utf-8') as f2:
        for line in f1:
            f2.write(str(int(line.strip('\n')) * 12) + '\n')
