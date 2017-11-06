import random


class Bear:
    def __init__(self):
        self.step_not_eat = 0

    def __str__(self):
        return "B"


class Fish:
    def __str__(self):
        return "F"


class System:
    def __init__(self, r, b, f, s, n):
        self.river_num = r
        self.percent_bear = int(0.01 * b * r)
        self.percent_fish = (0.01 * f * r)
        self.step_not_eat = s
        self.step = n
        self.river = []
        self.__river()

    def __river(self):
        for i in range(self.river_num):
            if i < self.percent_bear:
                self.river.append(Bear())
            elif i < self.percent_bear + self.percent_fish:
                self.river.append(Fish())
            else:
                self.river.append("_")
            random.shuffle(self.river)
        #print(self.river)
        self.__str__()
    def __str__(self):
        for i in range(self.river_num):
            if self.river[i]=="_":
                print("_",end="")
            elif self.river==Bear():
                print(self.river[i].__str__(),end="")
            else:
                print(self.river[i].__str__(),end="")

s=System(50,10,5,5,10)

