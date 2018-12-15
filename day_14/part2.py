recipes = [3,7]
elf_1 = 0
elf_2 = 1
my_input = [5,1,3,4,0,1]


def generate_next(recipes, elf_1, elf_2, my_input, count):
    found = False
    next_recipe = recipes[elf_1] + recipes[elf_2]
    if next_recipe > 9:
        next_recipe_1 = int(next_recipe / 10)
        next_recipe_2 = next_recipe % 10
        recipes.append(next_recipe_1)
        if recipes[-6:] == my_input:
            found = True
            count -= 1
        recipes.append(next_recipe_2)
        if recipes[-6:] == my_input:
            found = True
        count += 2
    else:
        recipes.append(next_recipe)
        if recipes[-6:] == my_input:
            found = True
        count += 1
    return recipes, found, count

def update_current_recipe(elf):
    return (elf + recipes[elf] + 1) % len(recipes)

found = False
count = 0
while not found:
    recipes, found, count = generate_next(recipes, elf_1, elf_2, my_input, count)
    elf_1 = update_current_recipe(elf_1)
    elf_2 = update_current_recipe(elf_2)

print(len(recipes))
print(recipes[-6:])
print(count-3)
    

