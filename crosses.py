class Game:

    def __init__(self):
        self.table = self.generate_table()
        self.print_table()

    def start_game(self):
        counter = 0

        while True:
            print(f'Хід гравця №{counter % 2 + 1}, Зробіть свій вибір')
            a, b = self.read_turn()

            if a > 15 or b > 15:
                print('Будьте уважніше, такої клітинки не існує')
                continue
            if self.table[a-1][b-1] != '_':
                print('Будьте уважніше, це місце вже зайняте')
                continue

            if counter % 2 == 0:
                symbol = 'X'
            else:
                symbol = 'O'

            self.table[a - 1][b - 1] = symbol
            self.detect_five_in_a_row_horizontal(a, b, symbol)
            self.print_table()
            counter += 1

    def generate_table(self):
        main_list = []
        for i in range(15):
            main_list.append(['_' for _ in range(1, 16)])
        return main_list

    def print_table(self):
        for i in self.table:
            for j in i:
                print(j, end=' | ')
            print()

    def read_turn(self):
        height_point = int(input('Виберіть висоту: '))
        width_point = int(input('Виберіть ширину: '))
        return height_point, width_point

    def detect_five_in_a_row_horizontal(self, x, y, sym):
        counter = 4
        for i in range(4):
            if self.table[x][y+i] == sym:
                counter += 1
            else:
                break
        for i in range(4):
            if self.table[x][y-i] == sym:
                counter += 1
            else:
                break
        if counter >= 5:
            print('тест пройдено')


    def win_conditions(self):
        pass


game = Game()
game.start_game()

# https://github.com/Nickwart/crosses.git
