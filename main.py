from pprint import pprint

def make_cook_book(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for dish in file:
            dishes = dish.strip()
            ingredients = int(file.readline())
            dishes_list = []
            for ing in range(ingredients):
                element = file.readline().split("|")
                dict_of_elements = {'ingredient_name': element[0].strip(), 'quantity': int(element[1]), 'measure': element[2].strip() }
                dishes_list.append(dict_of_elements)
                cook_book[dishes] = dishes_list
            file.readline()
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for part in cook_book[dish]:
                if part['ingredient_name'] not in shop_list:
                    shop_list[part['ingredient_name']] = {'measure': part['measure'], 'quantity': part['quantity']*person_count }
                else:
                    shop_list[part['ingredient_name']]['quantity'] += part['quantity']*person_count

        else:
            print('Такого блюда нет в рецептах, введите другие блюда и начните сначала')
            shop_list = {}
            break
    print(shop_list)

if __name__ == '__main__':
    cook_book = {}
    make_cook_book("recipes.txt")
    get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)



