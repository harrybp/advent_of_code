recipes = [3,7]
elf_1 = 0
elf_2 = 1
my_input = 513401


def generate_next(recipes, elf_1, elf_2):
    next_recipe = recipes[elf_1] + recipes[elf_2]
    if next_recipe > 9:
        next_recipe_1 = int(next_recipe / 10)
        next_recipe_2 = next_recipe % 10
        recipes.append(next_recipe_1)
        recipes.append(next_recipe_2)
    else:
        recipes.append(next_recipe)
    return recipes

def update_current_recipe(elf):
    return (elf + recipes[elf] + 1) % len(recipes)


while len(recipes) < my_input + 10:
    recipes = generate_next(recipes, elf_1, elf_2)
    elf_1 = update_current_recipe(elf_1)
    elf_2 = update_current_recipe(elf_2)
    
print(recipes[-10:])
