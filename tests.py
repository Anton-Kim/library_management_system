import builtins
from funcs import open_db, check_empty_input, add_book, del_book, search_book, show_books, change_stat


def inputer(inp):
    """Генератор для имитации пользовательского ввода"""
    ind = 0

    def next_element(*args):
        nonlocal ind
        res = inp[ind]
        ind += 1
        return res

    return next_element


class Tests:
    def test_check_empty_input(self):
        """Проверка пустого инпута"""
        builtins.input = inputer(['', '1'])
        assert '1' == check_empty_input('Тест')

    def test_add_book(self):
        """Проверка добавления книги в базу"""
        builtins.input = inputer(['Гарри Поттер', 'Джоан Кэтлин Роулинг', '1997'])
        add_book()
        data = open_db()
        last_id = list(data.keys())[-1]
        assert 'Гарри Поттер' in [j for i, j in data[last_id].items()]

    def test_search_book(self):
        """Проверка поиска книги"""
        builtins.input = inputer(['Гарри Поттер'])
        data = search_book()
        assert 'Гарри Поттер' in [i[1] for i in data]

    def test_show_books(self):
        """Проверка возврата словаря функцией вывода всех книг"""
        assert isinstance(show_books(), dict)

    def test_change_stat(self):
        """Проверка смены статуса книги"""
        data = open_db()
        last_id = list(data.keys())[-1]
        builtins.input = inputer([last_id, '1'])
        change_stat()
        data = open_db()
        assert data[last_id]['status'] == 'выдана'
        builtins.input = inputer([last_id, '1'])
        change_stat()
        data = open_db()
        assert data[last_id]['status'] == 'в наличии'

    def test_del_book(self):
        """Проверка удаления книги из базы"""
        data = open_db()
        last_id = list(data.keys())[-1]
        builtins.input = inputer([last_id, '1'])
        del_book()
        data = open_db()
        if data:
            last_id = list(data.keys())[-1]
            assert 'Гарри Поттер' not in [j for i, j in data[last_id].items()]
