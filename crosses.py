class Game:

    def __init__(self):
        self.table = self.generate_table()
        self.print_table()

    def start_game(self):
        counter = 0
        while True:
            print(f'Хід гравця №{counter % 2 + 1}, Зробіть свій вибір')
            a = self.read_turn_a()
            b = self.read_turn_b()

            if self.table[a-1][b-1] != '_':
                print('Будьте уважніше, це місце вже зайняте')
                continue

            if counter % 2 == 0:
                self.table[a - 1][b - 1] = 'X'

            elif counter % 2 == 1:
                self.table[a - 1][b - 1] = 'O'
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

    def read_turn_a(self):
        res = int(input('Виберіть висоту: '))
        return res

    def read_turn_b(self):
        res = int(input('Виберіть ширину: '))
        return res


game = Game()
game.start_game()

# https://github.com/Nickwart/crosses.git
