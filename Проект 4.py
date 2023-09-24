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
        print(f'{self.name.title()} прыгнул')
    def bark(self):
        '''Команда 'голос' '''
        print(f'{self.name.title()}:гав-гав')

my_dog = Dog('Гризи', 100, 'Немецкая овчарка')
my_dog.jump()

my_dog2 = Dog('Череп', 9, 'Дворняга')
print(my_dog2.name)
my_dog2.sit()