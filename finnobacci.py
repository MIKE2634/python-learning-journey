num = [0, 1]

while num[-1] + num[-2] > 200000000:
    pali = num[-2] + num[-1]
    num.append(pali)

print(num)