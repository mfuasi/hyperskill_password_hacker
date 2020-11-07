num = int(input())
new_num = (num).to_bytes(2, byteorder='little')

print(sum(bytearray(new_num)))
