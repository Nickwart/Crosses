class Game:

    def __init__(self):
        self.table = self.generate_table()
        self.print_table()

    def start_game(self):
        counter = 0
        while True:
            print(f'Хід гравця №{counter % 2 + 1} \nЗробіть свій вибір')
            a, b = int(input('Виберіть висоту: ')), int(input('Виберіть ширину: '))
            if counter % 2 == 0:
                if self.table[a][b] != 0:
                    print('Fatal error. Please be more attentive')
                    break
                self.table[a][b] = 'X'
                self.print_table()
                counter += 1
            elif counter % 2 == 1:
                if self.table[a][b] != 0:
                    print('Fatal error. Please be more attentive')
                    break
                self.table[a][b] = 'Y'
                self.print_table()
                counter += 1

    def generate_table(self):
        main_list = []
        for i in range(15):
            main_list.append([0 for _ in range(1, 16)])
        return main_list

    def print_table(self):
        for i in self.table:
            for j in i:
                print(j, end=' | ')
            print()
            print('-' * 59)


game = Game()
game.start_game()

# https://github.com/Nickwart/crosses.git
