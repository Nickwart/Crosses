import time
from random import randint


class Human:
    gender = None

    def __init__(self, name, age, inner_ass, outer_ass):
        self.name = name
        self.age = age
        self.inner_ass = inner_ass
        self.outer_ass = outer_ass

    @staticmethod
    def birth_timer():
        counter = 9
        while True:
            print(f'До народження лишилось {counter} (уявних) місяців')
            counter -= 1
            time.sleep(1)
            if counter == 0:
                print('О, ні, Сара! Воно таки вилізло!!!')
                break

    def possibility(self, num):
        poss = randint(0, 100)
        if poss in range(0, num):
            return True
        else:
            return False

    gender_list = ['male', 'female']
    inner_ass = ['pinky', 'RED', "nigga's black_door"]
    outer_ass = ['white', 'jew', 'nigger']

    @classmethod
    def add_outer_ass_color(cls, color):
        cls.outer_ass.append(color)

    def __add__(self, other):
        if self.gender == other.gender:
            print('Nothing happened, men')
        elif self.possibility(50):
            print('Nothing happened, fellow kids')
        else:
            child = Human(name='untitled', age=0, inner_ass=None, outer_ass='look at me, nigga')
            child.gender = None
            if self.possibility(50):
                child.gender = self.gender
            else:
                child.gender = other.gender


class Man(Human):
    def __init__(self, dick_length, gender='Male', *args, **kwargs):
        super(Man, self).__init__(*args, **kwargs)
        self.gender = gender
        self.dick_length = dick_length


class Woman(Human):
    def __init__(self, deepnest, gender='female', *args, **kwargs):
        super(Woman, self).__init__(*args, **kwargs)
        self.deepnest = deepnest
        self.gender = gender


Human.add_outer_ass_color('malinovy')

print(Human.outer_ass)
Human.birth_timer()
