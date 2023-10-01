import time


class House:
    def __init__(self, area: float, rooms: int, adres: str):
        '''
        :param area: площадь
        :param rooms: комнаты
        :param adres: адрес
        '''
        self.area = area
        self.rooms = rooms
        self.adres = adres

    def open_door(self):
        print(f'***Дверь дома по адресу {self.adres} открыта***')

    def close_door(self):
        print(f'***Дверь дома по адресу {self.adres} закрыта***')

    def get_door_statys(self):
        if self.close_door():
            return 'Дверь закрыта'
        else:
            return 'Дверь закрыта'


class MultiStoryHouse(House):
    def __init__(self, area: float, rooms: int, adres: str, floors: int):
        super().__init__(area, rooms, adres)
        self.floors =floors
        self.elevator_floor = 1
        self.elevator_door_closed = True

    def get_floors(self):
        return self.floors

    def call_elevatior(self, floor: int):
        '''
        :param floor: этаж куда вызывается лифт
        '''
        floor_time = 3
        way = abs(floor-self.elevator_floor)
        total_time = floor_time * way
        print(f'Лифт оправляется с {self.elevator_floor} на {floor}')
        time.sleep(total_time)
        self.elevator_floor = floor
        print('Лифт приехал')
        self.elevator_door_closed = False
        print('Дверь открывается ..........')
        time.sleep(5)
        print('Дверь открыта')
        time.sleep(10)
        self.elevator_door_closed = True
        print('Дверь закрыта')


##########################################################################


House1 = House(80, 4, 'г. Луганск, ул. Ворошиловской правды, 4')
House1.close_door()
print(f'Колтчество комнат: {House1.rooms}')
House1.get_door_statys()

House2 = MultiStoryHouse(300, 150, 'Нигде', 9)
House2.open_door()
House2.call_elevatior(7)
House2.call_elevatior(2)