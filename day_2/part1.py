with open('input.txt') as f:
    content = f.readlines()

two_count = 0
three_count = 0
for line in content:
    checked = []
    two_found = False
    three_found = False
    for letter in line:
        if letter in checked:
            continue
        if line.count(letter) == 2 and not two_found:
            two_count += 1
            two_found = True
        elif line.count(letter) == 3 and not three_found:
            three_count += 1
            three_found = True
        checked.append(letter)

print(two_count * three_count)