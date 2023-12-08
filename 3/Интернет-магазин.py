all_products = {'Весь склад': {}}
cart = {}

while True:
    action = input('Что вы хотите сделать? (добавить/продукты/корзина/удалить/выход): ')

    if action.lower() == 'выход':
        break
    elif action.lower() == 'добавить':
        product_name = input('Введите названия продукта: ')
        product_count = int(input('Введите количество: '))
        all_products['Весь склад'][product_name] = product_count
        print(f'Продукт "{product_name}" добавлен на склад')
    elif action.lower() == 'продукты':
        print('Список продуктов и их кол-во на складе:')
        for product, count in all_products['Весь складд'].items():
            print(f'{product}: {count}')
    elif action.lower() == 'корзина':
        print('Содержимое корзины:')
        for product, count in cart.items():
            print(f'{product}: {count}')
        cart_action = input('Что вы хотите сделать с корзиной? (добавить/заменить/удалить/назад): ')
        if cart_action.lower() == 'добавить':
            product_name = input('Введиите название продукта: ')
            product_count = int(input('Введите количество: '))
            if product_name in cart:
                cart[product_name] = product_count
            else:
                cart[product_name] = product_count
            print(f'Продкт "{product_name}" добавленн в корзину')
        elif cart_action.lower() == 'заменить':
            product_name = input('Введите название продукта: ')
            product_count = int(input('Введите новое количетво: '))
            cart[product_name] = product_count
            print(f'Количество продукта "{product_name}" в корзине изменено на {product_count}')
        elif cart_action.lower() == 'удалить':
            product_name = input('Введите название продукта: ')
            if product_name in cart:
                cart.pop(product_name)
                print(f'Продукт "{product_name}" удален из корзины')
            else:
                print(f'Продукт "{product_name}" не найден в корзине')
        elif cart_action.lower() == 'назад':
            break
        else:
            print('Неверрная команда')
    elif action.lower() == 'удалить':
        product_name = input('Введите название продукта: ')
        if product_name in all_products['Весь склад']:
            all_products['Весь склад'].pop(product_name)
            print(f'Продукт "{product_name}" удален со склада')
        else:
            print(f'Продукт "{product_name}" не найден на складе')
    else:
        print('Неверная команда')

print('Программа завершена')
