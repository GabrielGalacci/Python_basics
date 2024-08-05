# isinstance - para saber se o objeto é de determinado tipo
list = [
    'abc', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Gabriel'},
]

for item in list:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))
        print()

    elif isinstance(item, str):
        print('STR')
        print(f'{item} in uppercase is {item.upper()}')
        print()

    elif isinstance(item, (int, float)):
        print('NUMBERS')
        print(f'{item} x 2 is {item * 2}')
        print()

    else:
        print('OUTRO')
        print(item)
        print()