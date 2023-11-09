#  Задача №1
import os    
path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path) as recipes_file:
    cook_book = {}
    for string in recipes_file:
        dish = string.strip()
        ingredients_count = int(recipes_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredients_name, quantity, measure = recipes_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredients_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict
        recipes_file.readline()
        
#  Задача №2
def shop_list(dishes, person_count):
    shop_dict = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredients_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if shop_dict.get(ingredient['ingredient_name']) == 'None':
                union = (int(shop_dict[ingredient['ingredient_name']]['quantity']) + 
                         int(ingredients_list[ingredient['ingredient_name']]['quantity']))
                shop_dict[ingredient['ingredient_name']]['quantity'] = union
            else:
                shop_dict.update(ingredients_list)
    return shop_dict

print(shop_list(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5))

#  Задача №3
def create_file_list(folder):
    file_list = os.listdir(folder)
    merget_file_list = []
    for file in file_list:
        with open(folder + "/" + file) as _temp_file:
            merget_file_list.append([file, 0 ,[]])
            for line in _temp_file:
                merget_file_list[-1][2].append(line.strip())
                merget_file_list[-1][1] += 1
    return sorted(merget_file_list, key=lambda x: x[1], reverse=False)
    
def create_merget_file(folder, filename):
    with open(filename + '.txt', 'w+') as merget_file:
        merget_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            merget_file.write(f'Название файла: {file[0]}\n')
            merget_file.write(f'Количество строк: {file[1]}\n')
            for string in file[2]:
                merget_file.write(string + '\n')
            merget_file.write('\n')
    return print('Файл создан')

create_file_list('txt', 'merget_file')