# game.py

from gameparts import Board
# Из файла exceptions.py, который лежит в пакете gameparts,
# импортируется класс FieldIndexError.
from gameparts.exceptions import FieldIndexError

def main():
    game = Board()
    game.display()
    # Пользователь вводит номер строки.
    row = int(input('Введите номер строки: '))
    # Если введённое значение меньше нуля или больше или равно
    # field_size (это значение равно трём, оно хранится в модуле
    # parts.py)...
    if row < 0 or row >= game.field_size:
        # ...выбросить исключение FieldIndexError.
        raise FieldIndexError
   # game.py

...

    column = int(input('Введите номер столбца: '))
    if column < 0 or column >= game.field_size:
        raise FieldIndexError

    ...

if __name__ == '__main__':
   