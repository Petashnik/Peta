class House:
    houses_history = []

    def __new__(cls, *name, **number_of_floors):
        name = name[0]
        cls.houses_history.append(name)
        print(cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.numbers_of_floors = number_of_floors

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        house_name = str(f'Название: {self.name}, количество этажей: {self.numbers_of_floors}')
        return house_name

    def __eq__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors

    def __ne__(self, other):
        if isinstance(other.numbers_of_floors, int) and isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors = self.numbers_of_floors + value
        return  self

    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors = value + self.numbers_of_floors
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
        return self

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')


    # def go_to (self, new_floor):
    #     floor = 0
#     new_floor = int(new_floor)
    #     if new_floor < 1 or new_floor > self.numbers_of_floors:
    #         print (f'В Доме {self.name} этажа {new_floor} не существует')
    #     else:
#         print(f'{self.name}')
    #         for floor in range(new_floor):
    #             print(floor + 1)


h1 = House ('ЖК Эльбрус', 10)
h2 = House ('ЖК Акация', 20)
h3 = House ('ЖК Матрёшки', 20)
h4 = House ('ЖК Алые зори', 40)

# h1.go_to(18)
# h2.go_to(-1)
#
# #__str__
# print(h1)
# print(h2)
#
# #__len__
# print(len(h1))
# print(len(h2))



# print(h1)
# print(h2)
# print(h3)

#__eq__
# print(h1==h2)

#__add__
# h1 = h1.__add__(10)
# print(h1)
# print(h1 == h2)

#__iadd__
# h1 += h1.__iadd__(10)
# print (h1)

#__radd__
# h2 = h2.__radd__(10)
# print(h2)

#__gt__
# print(h1 > h2)

#__ge__
# print(h1 >= h2)

#__lt__
# print(h1 < h2)

#__le__
# print(h1 <= h2)

#__ne__
# print(h1 != h2)

#Удаление объектов

del h2
del h3
del h4

print(House.houses_history)

#Павел Ившин




