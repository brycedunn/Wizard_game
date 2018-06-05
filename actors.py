import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('The wizard {} attacks the {}'.format(
            self.name, creature.name
        ))

        my_roll = random.randint(5, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print('You rolled {}'.format(my_roll))
        print('{} rolls {}'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('You have triumphed over the {}'.format(creature.name))
            return True
        else:
            print('You have been DEFEATED!')
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

