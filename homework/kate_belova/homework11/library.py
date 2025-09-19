class Book:
    # fmt: off
    def __init__(self, title, author, page_count,
                 isbn, page_material='Офсетная бумага',
                 has_text=True, is_reserved=False):

        self.page_material = page_material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.is_reserved = is_reserved
    # fmt: on

    def __str__(self):
        base = (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.page_count}, материал: {self.page_material}'
        )
        if self.is_reserved:
            return f'{base}, зарезервирована'
        return base


free_music = Book(
    title='Как музыка стала свободной',
    author='Стивен Уитт',
    page_count=304,
    isbn='978-5-9903760-8-3',
    is_reserved=True,
)

fisher = Book(
    title='Фишер. По следу зверя. Настоящая история серийного убийцы',
    author='Александр Рогоза',
    page_count=384,
    isbn='978-5-4470-0749-2',
)

facing_life = Book(
    title='Один на один с жизнью',
    author='Илья Латыпов',
    page_count=592,
    isbn='978-5-9614-9026-8',
)

gravity_center = Book(
    title='Центр тяжести',
    author='Алексей Поляринов',
    page_count=528,
    isbn='978-5-00139-841-7',
)

the_granddaughter = Book(
    page_material='Газетная бумага',
    title='Внучка',
    author='Бернхард Шлинк',
    page_count=416,
    isbn='978-5-389-24133-6',
)

books = [free_music, fisher, facing_life, gravity_center, the_granddaughter]
for book in books:
    print(book)

print('-' * 100)


class Textbook(Book):
    # fmt: off
    def __init__(
            self, title, author, page_count, isbn,
            subject, grade, page_material='Офсетная бумага',
            has_text=True, has_exercises=True, is_reserved=False,
    ):
        super().__init__(
            title, author, page_count, isbn,
            page_material, has_text, is_reserved,
        )

        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises
    # fmt: on

    def __str__(self):
        base = (
            f'Название: {self.title}, Автор: {self.author}, '
            f'страниц: {self.page_count}, предмет: {self.subject}, '
            f'класс: {self.grade}'
        )
        if self.is_reserved:
            return f'{base}, зарезервирована'
        return base


algebra = Textbook(
    title='Алгебра',
    author='Иванов',
    page_count=200,
    isbn='978-5-11111-111-1',
    subject='Математика',
    grade=9,
)

history = Textbook(
    title='История России',
    author='Петров',
    page_count=350,
    isbn='978-5-22222-222-2',
    subject='История',
    grade=10,
)

biology = Textbook(
    title='Биология. Человек и его здоровье',
    author='Смирнова',
    page_count=320,
    isbn='978-5-44444-444-4',
    subject='Биология',
    grade=8,
)

english = Textbook(
    title='Английский язык. New Challenges',
    author='Быкова',
    page_count=250,
    isbn='978-5-55555-555-5',
    subject='Английский язык',
    grade=6,
    is_reserved=True,
)

textbooks = [algebra, history, biology, english]
for book in textbooks:
    print(book)
