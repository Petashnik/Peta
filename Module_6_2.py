class Vehicle:
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)

    __COLOR_VARIANTS = ['Red', 'White', 'Black', 'Grey', 'Blue']

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print (f'Владелец: {self.owner}')

    def set_color(self, _color):
        color_up = [_color.lower() for _color in self.__COLOR_VARIANTS]
        if _color.lower() in color_up:
            self.__color = _color
        else:
            print(f'Нельзя сменить цвет на {_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()
