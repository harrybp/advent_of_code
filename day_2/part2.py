with open('input.txt') as f:
    content = f.readlines()

for line1 in content:
    for line2 in content:
        difference = 0
        for x in range(len(line1)):
            if line1[x] != line2[x]:
                difference += 1
            if difference > 1:
                break
        if difference == 1:
            print(line1)
            print(line2)
            break