# Описать транспортное средство. Можете брать любое на свое усмотрение. Хочу видеть наследование (обычное с несколькими
# уровнями иерархии), абстракцию, сокрытие, инкапсуляцию.
# *** Реализовать фабричный метод паттерн проектирования на примере браузера.
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @property
    @abstractmethod
    def speed(self) -> int:
        ...
        # raise NotImplementedError()

    @abstractmethod
    def move(self):
        ...


class Motor_Vehicle(Vehicle, ABC):

    @property
    @abstractmethod
    def engine_type(self) -> str:
        ...


class Car(Motor_Vehicle):
    def __init__(self, speed: int, engine_type: str):
        self.__speed = speed
        self.__engine_type = engine_type

    @property
    def speed(self) -> int:
        return self.__speed

    @property
    def engine_type(self) -> int:
        return self.__engine_type

    @classmethod
    def move(cls):
        print('I go somewhere on the road')


if __name__ == '__main__':
    toyota = Car(12, 'eco')
    print(toyota.speed)
