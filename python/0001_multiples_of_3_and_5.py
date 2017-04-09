
max = 1000
sum = 0

for n in range(1, max):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

print(sum)
