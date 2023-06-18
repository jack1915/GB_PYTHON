def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Женя', cat={'Кузя': 2, 'Вася': 3}, turtle=['боб', 'женя', 'петя'],
                     hamster={'гном', 'пупс'}))