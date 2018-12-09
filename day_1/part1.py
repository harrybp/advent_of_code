with open('input.txt') as f:
    content = f.readlines()

total = 0
for line in content:
    number = int(line)
    total += number

print(total)