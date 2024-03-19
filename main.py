class Apartment:
    def __init__(self, num_rooms, area):
        self.__num_rooms = num_rooms
        self.__area = area

    def get_num_rooms(self):
        return self.__num_rooms

    def get_area(self):
        return self.__area


apartment = Apartment(4, 45)
print(f'{apartment.get_num_rooms()=}')
print(f'{apartment.get_area()=}')

