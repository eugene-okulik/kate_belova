class Flower:
    def __init__(self, name, color, stem_length, price, freshness, life_time):
        """
        name: название цветка
        color: цвет лепестков
        stem_length: длина стебля (см)
        price: цена одного цветка
        freshness: свежесть (0–10)
        life_time: среднее время жизни (в днях)
        """
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.freshness = freshness
        self.life_time = life_time

    def __repr__(self):
        return f'{self.name} ({self.color})'


class Rose(Flower):
    def __init__(self, color, stem_length, freshness):
        super().__init__(
            name='Роза',
            color=color,
            stem_length=stem_length,
            price=200,
            freshness=freshness,
            life_time=7,
        )


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness):
        super().__init__(
            name='Тюльпан',
            color=color,
            stem_length=stem_length,
            price=120,
            freshness=freshness,
            life_time=5,
        )


class Lily(Flower):
    def __init__(self, color, stem_length, freshness):
        super().__init__(
            name='Лилия',
            color=color,
            stem_length=stem_length,
            price=250,
            freshness=freshness,
            life_time=6,
        )


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def cost(self):
        return sum(f.price for f in self.flowers)

    def average_life_time(self):
        return sum(f.life_time for f in self.flowers) / len(self.flowers)

    def sort_by(self, attribute):
        """Сортировка по атрибуту
        ('freshness', 'color', 'stem_length', 'price')
        """
        self.flowers.sort(key=lambda f: getattr(f, attribute))

    def find(self, **kwargs):
        """
        Поиск цветов по параметрам.
        Например: bouquet.find(color='красный', stem_length=50)
        """
        result = self.flowers
        for key, value in kwargs.items():
            result = [f for f in result if getattr(f, key) == value]
        return result

    def __repr__(self):
        return f"Букет: {', '.join(str(f) for f in self.flowers)}"


rose1 = Rose(color='красный', stem_length=60, freshness=9)
rose2 = Rose(color='белый', stem_length=55, freshness=8)
tulip1 = Tulip(color='желтый', stem_length=40, freshness=7)
lily1 = Lily(color='розовый', stem_length=70, freshness=10)

bouquet = Bouquet([rose1, rose2, tulip1, lily1])

print(bouquet)
print('Стоимость:', bouquet.cost())
print('Среднее время жизни:', bouquet.average_life_time())
print('Поиск белых:', bouquet.find(color='белый'))

bouquet.sort_by('freshness')
print('После сортировки по свежести:', bouquet)
