temp = 0
lines = 0
with open('chicken.txt', 'r', encoding='UTF8') as f:
    for line in f:
        list = line.strip().split(": ")
        sum = int(list[1])
        temp += sum
        lines += 1

print("하루 평균 매출 : {}원".format(temp // lines))
