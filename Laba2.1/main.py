from typing import Union
import doctest


class SetLunch:
    def __init__(self, first_course: str, second_course: str, drink: str):
        """
        Создание и подготовка к работе объекта "Комплексный Обед"

        :param first_course: Первое блюдо
        :param second_course: Второе блюдо
        :param drink: Напиток
        """
        if not isinstance(first_course, str):
            raise TypeError("Название блюда должно состоять из букв (тип 'str')")
        self.first_course = first_course
        if not isinstance(second_course, str):
            raise TypeError("Название блюда должно состоять из букв (тип 'str')")
        self.second_course = second_course
        if not isinstance(drink, str):
            raise TypeError("Название напитка должно состоять из букв (тип 'str')")
        self.drink = drink
        self.amount_first_course = 1  # Стандартное количество первых блюд
        self.amount_second_course = 1  # Стандартное количество вторых блюд
        self.amount_drink = 1  # Стандартное количество напитков

    def get_price(self) -> int:
        """
        Функция для получения стоимость обеда
        :return: стоимость обеда
        """
        return (self.amount_first_course * 70) + (self.amount_second_course * 140) + (self.amount_drink * 15)  #70, 140, 15 - ценники

    def change_amount_first_course(self, amount: int):
        """
        Функция для изменения количества первого блюда

        :param amount: новое количество первого блюда
        :return:
        """
        if not isinstance(amount, int):
            raise TypeError("Количество первых блюд должно быть целочисленным")
        if amount < 0:
            raise ValueError("Количество первых блюд не должно быть отрицательным")
        self.amount_first_course = amount

    def change_amount_second_course(self, amount: int):
        """
        Функция для изменения количества второго блюда

        :param amount: новое количество второго блюда
        :return:
        """
        if not isinstance(amount, int):
            raise TypeError("Количество вторых блюд должно быть целочисленным")
        if amount < 0:
            raise ValueError("Количество вторых блюд не должно быть отрицательным")
        self.amount_second_course = amount

    def change_amount_drink(self, amount: int):
        """
                Функция для изменения количества напитков

                :param amount: новое количество напитков
                :return:
                """
        if not isinstance(amount, int):
            raise TypeError("Количество напитков должно быть целочисленным")
        if amount < 0:
            raise ValueError("Количество напитков не должно быть отрицательным")
        self.amount_drink = amount

# В следующих классах методы не будут реализованы


class Competition:
    def __init__(self, amount_players: int, amount_winners: int):
        """
        Создание и подготовка к работе объекта "Соревнование"

        :param amount_players: Количество игроков
        """
        if not isinstance(amount_players, int):
            raise TypeError("Количество игроков должно быть целочисленным")
        if amount_players <= 0:
            raise ValueError("Количество игроков должно быть положительным")
        dict_players = {num_player: 0 for num_player in range(1, amount_players + 1)}  #Создание словоря номер_игрока: количество баллов
        self.current_score = dict_players
        if not isinstance(amount_winners, int):
            raise TypeError("Количество победителей должно быть целочисленным")
        if amount_winners < 0:
            raise ValueError("Количество победителей не должно быть отрицательным")
        self.amount_winners = amount_winners

    def add_point(self, points: Union[int, float]):
        """
        Функция по добавлению (отниманию) очков определенному игроку
        :param points: Количество добавленных (отнятых) очков
        :raise TypeError: Очки надо указывать в цифрах (int или float)
        :return: измененный словарь current_score
        """
        pass

    def get_winner(self) -> int:
        """
        Функция по определению победителя в соревновании. Определиться он должен по наибольшему количеству очков
        :return: номер победителя
        """
        pass


class Computer:
    def __init__(self, ram: Union[int, float], cpu: Union[str, int, float], gpu: Union[str, None, int, float]):
        """
        Создание и подготовка к работе объекта "Компьютер"
        :param ram: Количество оперативной памяти
        :param cpu: Название процессора
        :param gpu: Название видеокарты
        """
        if not isinstance(ram, int):
            raise TypeError("Количество ОЗУ должно быть числом")
        if ram <= 0:
            raise ValueError("Количество ОЗУ должно быть положительным")
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu

    def change_ram(self, new_ram: Union[int, float]) -> Union[int, float]:
        """
        Функция по изменения количесвта ОЗУ
        :param new_ram: Новое количество ОЗУ
        :return:
        """
        pass

    def change_cpu(self, new_cpu: Union[str, int, float]) -> Union[str, int, float]:
        """
        Функция по изменения ЦП
        :param new_ram: Новый ЦП
        :return:
        """
        pass

    def change_gpu(self, new_gpu: Union[str, int, float]) -> Union[str, int, float]:
        """
        Функция по изменению ГП
        :param new_ram: Новый ГП
        :return:
        """
        pass


if __name__ == "__main__":
    doctest.testmod()
