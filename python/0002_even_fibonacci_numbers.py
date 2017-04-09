
def fibonacci(max):
    seq = [1,2]
    yield 1
    yield 2
    while True:
        seq.append(seq[-2] + seq[-1])
        if seq[-1] >= max:
            break
        yield seq[-1]

sum = 0

for x in fibonacci(4000000):
    if x % 2 == 0:
        sum += x

print(sum)
