with open('input.txt') as f:
    content = f.readlines()

dictionary = {}
total = 0
index = 0
while True:
    number = int(content[index])
    
    total += number
    print(total)
    if total in dictionary:
        break
    dictionary[total] = True
    index = (index + 1) % len(content)




print(total)