import random

import copy


class Animal:
    pass


class Fish(Animal):
    def __str__(self):
        return "F"


class Bear(Animal):
    def __init__(self):
        self.withoutFood = 0

    def __str__(self):
        return 'B'


class Ecosystem:
    def __init__(self, bear_dead, bear_percent, fish_percent, length_river, step):
        self.len_river = length_river
        self.num_bear = int(0.01 * self.len_river * bear_percent)
        self.num_fish = int(0.01 * self.len_river * fish_percent)
        self.empy = self.len_river - (self.num_bear + self.num_fish)
        self.steps = step
        self.river = []
        self.step_to_die = bear_dead
        self.__circle()

    def __str__(self):
        for i in range(self.len_river):
            if self.river[i] is None:
                print('_', end=' ')
            else:
                print(self.river[i].__str__(), end=' ')

    def __circle(self):
        self.__filling()
        if self.steps > 0:
            for i in range(self.steps-1):
                if self.num_fish == self.len_river or self.num_bear == self.len_river:
                    break
                print()
                self.__stepLife()
        else:
            s = ''
            while s != 'stop' and self.num_fish != self.len_river and self.num_bear != self.len_river:
                s = input()
                self.__stepLife()

    def __filling(self):
        for i in range(self.num_bear):
            self.river.append(Bear())
        for i in range(self.num_fish):
            self.river.append(Fish())
        for i in range(self.num_fish + self.num_bear, self.len_river):
            self.river.append(None)
        random.shuffle(self.river)
        self.__str__()


    def __stepLife(self):
        nextStep = -1
        for i in range(0, len(self.river)):
            if nextStep == -1:
                if type(self.river[i]) == Bear:
                    nextStep = self.__step_bear(i)
                if type(self.river[i]) == Fish:
                    nextStep = self.__step_fish(i)
            else:
                nextStep = -1
        self.__str__()

    def __step_bear(self, i):
        x = self.river[i].withoutFood
        step = self.getstep(i, self.len_river)
        if type(self.river[i + step]) == Fish:
            self.river[i] = None
            self.num_fish -= 1
            self.empy += 1
            self.river[i + step] = Bear()
        elif type(self.river[i + step]) == Bear:
            self.__child('bear')
            if x == self.step_to_die - 1:
                self.river[i] = None
                self.num_bear -= 1
                self.empy += 1
                return
            self.river[i].withoutFood += 1
            return -1
        else:
            self.river[i] = None
            if x == self.step_to_die - 1:
                self.num_bear -= 1
                self.empy += 1
                return
            self.river[i + step] = Bear()
            self.river[i + step].withoutFood = x + 1
        return step

    def __step_fish(self, i):
        step = self.getstep(i, self.len_river)
        if type(self.river[i + step]) == Bear:
            self.river[i] = None
            self.empy += 1
            self.num_fish -= 1
            self.river[i + step].withoutFood = 0
            return -1
        elif type(self.river[i + step]) == Fish:
            self.__child('fish')
            return -1
        else:
            self.river[i] = None
            self.river[i + step] = Fish()
        return step

    @staticmethod
    def getstep(i, lengthRiver):
        if i == 0:
            return 1
        elif i == lengthRiver - 1:
            return -1
        else:
            return random.randint(-1, 1)

    def __child(self, obj):
        index = self.__random_index()
        if index != -1:
            self.river[index] = Bear() if obj == 'bear' else Fish()
            self.empy -= 1
            if obj == 'bear':
                self.num_bear += 1
            else:
                self.num_fish += 1

    def __random_index(self):
        if self.empy != 0:
            item = random.randint(1, self.empy)
            number = 0
            for i in range(self.len_river):
                if self.river[i] is None:
                    number += 1
                    if number == item:
                        return i
        else:
            return -1


length_river = int(input('река: '))
step_to_die = int(input('число шагов медведя без еды: '))
bear = int(input("процент медведей: "))
fish = int(input('процент рыбы: '))
step = int(input('число шагов (0 для ручного прохода): '))
if step == 0:
    print('чтобы прейти к след. шагу нажмите Enter, для завершения введите "stop"')
e = Ecosystem(step_to_die, bear, fish, length_river, step)