import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print (f'{self.name} attack {other.name} !')
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print (f'{self.name} take {damage}! Health right now: {self.health}')

    def is_alive(self):
        return  self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack_power = 20)
    def special_attack(self, other):
        damage = random.randint(5, self.attack_power * 2)
        print(f'{self.name} do special attack for {other.name} !')
        other.take_damage(damage)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health = 75, attack_power = 15)
    def magic_attack (self, other):
        damage = random.randint(10, self.attack_power + 10)
        print(f'{self.name} do magic attack for {other.name} !')
        other.take_damage(damage)

def battle(character1, character2):
    while character1.is_alive and character2.is_alive:
        action = random.choice (['attack', 'spec_attack'])

        if isinstance(character1, Warrior) and action == 'spec_attack':
            character1.special_attack(character2)
        else:
            character1.attack(character2)

        if not character2.is_alive():
            print (f'{character2.name} is dead')
            break

        action = random.choice(['attack', 'spec_attack'])
        if isinstance(character2, Warrior) and action == 'spec_attack':
            character2.special_attack(character1)
        else:
            character2.attack(character1)

        if not character1.is_alive():
            print (f'{character1.name} is dead! Your are lose')
            break

def main():
    print('Welcome to Hero`s adventure!')
    player_name = input('Type name of your hero: ')

    choice = input ('Choice your class (Warrior / Mage): ').lower()

    if choice == 'Warrior':
        player = Warrior(player_name)

    elif choice == 'Mage':
        player = Mage(player_name)

    else:
        print ('Don`t match type, create Warrior default class')
        player = Warrior(player_name)

    enemy = Warrior ('Skeleton-Archer')

    print (f'\n{player_name} begin battle with {enemy.name}')

    battle (player, enemy)

if __name__ == '__main__':
    main()


