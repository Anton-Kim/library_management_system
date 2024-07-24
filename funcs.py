from json import dump, load


def open_db() -> dict:
    """Открытие базы библиотеки из json-файла"""
    try:
        with open('db.json') as file:
            data: dict = load(file)
        return data
    except Exception as e:
        print(e)


def close_db(data) -> None:
    """Закрытие базы библиотеки с сохранением в json-файл"""
    try:
        with open('db.json', 'w') as file:
            dump(data, file)
    except Exception as e:
        print(e)


def check_empty_input(prompt) -> str:
    """Проверка на пустой инпут от пользователя"""
    value: str = input(prompt)
    while not value:
        value: str = input(f'Поле не должно быть пустым. {prompt}')
    return value.strip()


def add_book() -> None:
    """Добавление книги в базу с уникальным id и статусом по-умолчанию 'в наличии'"""
    db: dict = open_db()
    id: int = max([int(i) for i in db.keys()]) + 1 if db else 1
    title: str = check_empty_input('Введите название книги: ')
    author: str = check_empty_input('Введите автора книги: ')
    year: str = check_empty_input('Введите год издания книги: ')
    status: str = 'в наличии'
    db[id]: dict = {'title': title, 'author': author, 'year': year, 'status': status}
    close_db(db)
    print(f'\nКнига успешно добавлена в библиотеку под id {id}.')


def del_book() -> None:
    """Удаление книги из базы"""
    id: str = check_empty_input('Введите id книги, которую нужно удалить: ')
    db: dict = open_db()
    if id in db:
        print(f'Безвозвратно удалить книгу с id {id}?')
        var: str = check_empty_input('1. Да   2. Нет: ')
        if var == '1':
            del db[id]
            close_db(db)
            print(f'\nКнига с id {id} успешно удалена из библиотеки.')
        elif var == '2':
            pass
        else:
            print('\nВведен несуществующий вариант.')
    else:
        print(f'\nКнига с id {id} отсутствует в бибилиотеке.')


def search_book() -> list:
    """Поиск книг по полям 'title', 'author', 'year' в базе"""
    text: str = check_empty_input('Введите автора, название книги или год издания: ').lower()
    db: dict = open_db()
    res: list = []
    for book in db:
        i, t, a, y = book, db[book]['title'], db[book]['author'], db[book]['year']
        if text in t.lower() or text in a.lower() or text in y.lower():
            res.append([i, t, a, y])
    return res


def show_books() -> dict:
    """Вывод всех книг, имеющихся в базе"""
    db: dict = open_db()
    return db


def change_stat() -> None:
    """Смена статуса книги"""
    id: str = check_empty_input('Введите id книги, статус которой надо изменить: ')
    db: dict = open_db()
    if id in db:
        status_now: str = db[id]['status']
        status_after: str = 'выдана' if status_now == 'в наличии' else 'в наличии'
        print(f'Сейчас статус книги с id {id} - "{status_now}". Хотите сменить его на "{status_after}"?')
        var: str = check_empty_input('1. Да   2. Нет: ')
        if var == '1':
            db[id]['status']: str = status_after
            close_db(db)
            print(f'\nСтатус книги c id {id} успешно изменен на "{status_after}".')
        elif var == '2':
            pass
        else:
            print('\nВведен несуществующий вариант.')
    else:
        print(f'\nКнига с id {id} отсутствует в бибилиотеке.')
