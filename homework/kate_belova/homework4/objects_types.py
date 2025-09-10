my_dict = {
    'tuple': (
        'Django',
        'FastAPI',
        'Telegram Bots',
        'Machine Learning',
        'QA Automation',
    ),
    'list': ['English', '直線移動', 'Русский', 'Deutsch', 'Українська'],
    'dict': {
        'Stephen King': [
            'The Dead Zone (1979)',
            'Hearts in Atlantis (1999)',
            '11/22/63 (2011)',
        ],
        'Макс Фрай, Линор Горалик': ['Книга Одиночеств (2004)'],
        'Fredrik Backman': ['En man som heter Ove (2012)'],
        'Donna Tartt': ['The Goldfinch (2013)'],
        'Дмитрий Глуховский': ['Будущее (2013)'],
        'Катерина Гордеева': ['Унеси ты мое горе (2023)'],
        'Nathan Hill': ['Wellness (2023)'],
        'Саша Филипенко': ['Слон (2025)'],
    },
    'set': {2, 49, 34, 5, 10, 100, 100, 125},
}

print(f'The most interesting in Python development: {my_dict['tuple'][-1]}\n')

my_dict['list'].append('Беларуская')
del my_dict['list'][1]

my_dict['dict']['i am a tuple'] = ['Peace', 'Love', '&', 'Understanding']
del my_dict['dict']['Дмитрий Глуховский']

my_dict['set'].add(1000)
my_dict['set'].remove(34)

print(my_dict)
