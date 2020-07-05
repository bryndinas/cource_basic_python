class Road:

    def __init__(self, length, width):
        self.__width = width
        self.__length = length

    def massa_as(self):
        result = self.__width * self.__length * 25 * 5
        itog = result / 1000

        print(f'Для покрытия дороги нужно {itog} тонн асфальта')

s = Road(12,50)
s.massa_as()
