class Game:

    def __init__(self):
        self.table = self.generate_table()
        self.print_table()

    def start_game(self):
        counter = 0
        while True:
            print(f'Хід гравця №{counter % 2 + 1}, Зробіть свій вибір')
            coords = input('Виберіть висоту та ширину: ')
            a, b = int(coords[0]), int(coords[1])

            if self.table[a-1][b-1] != '_':
                print('Fatal error. Please be more attentive')
                break

            if counter % 2 == 0:
                self.table[a - 1][b - 1] = 'X̲'

            elif counter % 2 == 1:
                self.table[a - 1][b - 1] = 'O̲'
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


game = Game()
game.start_game()

# https://github.com/Nickwart/crosses.git
