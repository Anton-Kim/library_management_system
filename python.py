from funcs import *
from tests import Tests


class Menu:
    """Класс меню консольного приложения"""

    def __init__(self):
        self.ask_item: str = 'Введите пункт меню: '

    def loop(self):
        """Основной цикл меню"""
        actions: dict = {
            '1': add_book,
            '2': del_book,
            '3': search_book,
            '4': show_books,
            '5': change_stat,
        }
        while True:
            print('1. Добавление книги\n2. Удаление книги\n3. Поиск книги\n4. Отображение всех книг\n5. '
                  'Изменение статуса книги\n')
            action = actions.get(input(self.ask_item).strip())
            if action:
                self.ask_item: str = 'Введите пункт меню: '
                if action == search_book:
                    res = search_book()
                    if res:
                        print('\nРезультаты поиска:')
                        print('=' * 62)
                        for r in res:
                            print(f'{r[0]}, {r[1]}, {r[2]}, {r[3]}')
                    else:
                        print('\nК сожалению по вашему запросу ничего не найдено.')
                elif action == show_books:
                    db = show_books()
                    if db:
                        print(f'\nid      title            author            year      status')
                        print('=' * 62)
                        for book in db:
                            t, a, y, s = db[book]['title'], db[book]['author'], db[book]['year'], db[book]['status']
                            print(book.ljust(8, ' ') if len(book) < 8 else book[:4] + '... ', end='')
                            print(t.ljust(17, ' ') if len(t) < 17 else t[:13] + '... ', end='')
                            print(a.ljust(18, ' ') if len(a) < 18 else a[:14] + '... ', end='')
                            print(y.ljust(10, ' ') if len(y) < 10 else y[:6] + '... ', end='')
                            print(s)
                    else:
                        print('\nКниги в билиотеке пока что отсутствуют.')
                else:
                    action()
                print()
            else:
                self.ask_item: str = 'Введен некорректный пункт меню. Введите цифру: '


if __name__ == '__main__':
    """Запуск тестов с эмуляцией пользовательского ввода"""
    # origin_input = __builtins__.input
    # tests = Tests()
    # for t in tests.__dir__():
    #     if t.startswith('test_'):
    #         getattr(tests, t)()
    # __builtins__.input = origin_input

    """Запуск меню"""
    menu = Menu()
    menu.loop()
