class Dog:
    def __init__(self, name: str, age: int, breed: str):
        '''
        :param name: кличка собаки
        :param age: возраст собаки
        '''
        self.name = name
        self.age = age
        self.breed = breed
        print('Собака создана')

    def sit(self):
        '''Команда "сидеть" '''
        print(f'{self.name.title()} сел')
    def jump(self):
        '''Команда 'прыжок' '''
        jump_heights = {
            'Дворняга':0.5,
            'Шпиц':999999999999999999999999999999,
            'Немецкая овчарка': 10
        }
        if self.breed in jump_heights:
            height = jump_heights[self.breed]
            print(f'{self.name.title()} прыгнул на {height} метров')
        else:
            print(f'{self.name.title()} сделал прыжок')
    def bark(self):
        '''Команда 'голос' '''
        print(f'{self.name.title()}:гав-гав')

##################################################################################################


my_dog = Dog('Гризи', 100, 'Немецкая овчарка')
my_dog.jump()



my_dog2 = Dog('Череп', 9, 'Дворняга')
print(my_dog2.name)
my_dog2.sit()
my_dog2.jump()
