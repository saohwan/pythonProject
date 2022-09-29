i = 0
sum = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    sum = sum + i

print(sum)
