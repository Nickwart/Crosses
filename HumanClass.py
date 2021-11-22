from random import randint


class Human:
    gender = None

    def __init__(self, name, age, inner_ass, outer_ass):
        self.name = name
        self.age = age
        self.inner_ass = inner_ass
        self.outer_ass = outer_ass

    @staticmethod
    def possibility(num):
        poss = randint(0, 100)
        if poss in range(0, num):
            return True
        else:
            return False

    choices = {gender: {male: 'male', fmale: 'female'},
               inner_ass: {one: 'pinky', two: 'RED', three: "nigga's black whole"}
               outer_ass: {}
               }

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
            for key, value in self.choices:
                pass


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
