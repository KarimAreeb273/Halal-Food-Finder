from db.models import Restaurant

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def create_restaurant_table(restaurants):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for restaurant in restaurants:
        id_spaces = 4 - len(str(restaurant.id))
        name_spaces = 43 - len(restaurant.name)
        print(f'|{restaurant.id}{" " * id_spaces}|{restaurant.name}{" " * name_spaces}|')
    print('-' * 50)

def create_location_table(locations):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for location in locations:
        id_spaces = 4 - len(str(location.id))
        name_spaces = 43 - len(location.name)
        print(f'|{location.id}{" " * id_spaces}|{location.name}{" " * name_spaces}|')
    print('-' * 50)

def create_menu_table(restaurants):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for restaurant in restaurants:
        id_spaces = 4 - len(str(restaurant.id))
        name_spaces = 43 - len(restaurant.menu)
        print(f'|{restaurant.id}{" " * id_spaces}|{restaurant.menu}{" " * name_spaces}|')
    print('-' * 50)
