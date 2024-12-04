class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        house_name = str(f'Название: {self.name}, количество этажей: {self.numbers_of_floors}')
        return house_name


    # def go_to (self, new_floor):
    #     floor = 0
#     new_floor = int(new_floor)
    #     if new_floor < 1 or new_floor > self.numbers_of_floors:
    #         print (f'В Доме {self.name} этажа {new_floor} не существует')
    #     else:
#         print(f'{self.name}')
    #         for floor in range(new_floor):
    #             print(floor + 1)


h1 = House ('ЖК Эльбрус', 30)
h2 = House ('Домик в деревне', 2)

# h1.go_to(18)
# h2.go_to(-1)

#__str__
print(h1)
print(h2)

#__len__
print(len(h1))
print(len(h2))


#Павел Ившин




