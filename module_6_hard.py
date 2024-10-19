from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides: int):
        if self.__is_valid_color(color):
            self.__color = color

        if self.__is_valid_sides(list(sides)):
            self.__sides = list(sides)

    @staticmethod
    def __is_valid_color(color: tuple[int, int, int]):
        if len(color) != 3:
            return False
        for number in color:
            if not isinstance(number, int):
                return False
            if not (0 <= number <= 255):
                return False
        return True

    def __is_valid_sides(self, sides: list[int]):
        if len(sides) != self.sides_count:
            return False
        for number in sides:
            if not (number > 0):
                return False
            if not isinstance(number, int):
                return False
        return True

    def set_color(self, r: int, g: int, b: int):
        color = (r, g, b)
        if self.__is_valid_color(color):
            self.__color = color

    def get_color(self):
        return self.__color

    def set_sides(self, *sides: int):
        if self.__is_valid_sides(list(sides)):
            self.__sides = list(sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], *sides: int):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def set_sides(self, *sides: int):
        super().set_sides(*sides)
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self.get_sides()
        p = len(self)
        return sqrt(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int):
        super().__init__(color, *([side] * 12))

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
