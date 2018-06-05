import random
import time
from actors import Wizard, Creature


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------------')
    print('      Seven Sorcerers')
    print('----------------------------')


def game_loop():
    creatures = [
        Creature('Rabbit', 1),
        Creature('Kobold', 7),
        Creature('Wyrm', 22),
        Creature('Bandit', 18),
        Creature('Evil Sorcerer', 100)
    ]

    hero = Wizard('Bryce', 5)

    while True:

        active_creature = random.choice(creatures)
        print('A {}, lvl {} has appeared!'.format(active_creature.name, active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('You slowly crawl away and hide, taking time to recover.')
                time.sleep(5)
                print('The wizard return revitalized!')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'
                  .format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting game. Bye!')
            break


if __name__ == '__main__':
    main()
