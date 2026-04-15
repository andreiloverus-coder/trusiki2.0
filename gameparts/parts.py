# gameparts/parts.py

...

    def display(self):
        ...

    def is_board_full(self):
        # Цикл проходится по всем столбцам игрового поля.
        for i in range(self.field_size):
            # А потом по всем строчкам.
            for j in range(self.field_size):
                # Если находит свободную ячейку...
                if self.board[i][j] == ' ':
                    # ...игра продолжается.
                    return False
        # Иначе - ничья!
        return True

...