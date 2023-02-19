from typing import Union


class Computer:
    def __init__(self, cpu: str, ram: int, gpu: Union[str, None]):
        """
        Создание и подготовка к работе объекта "Компьютер"
        :param cpu: Название процессора
        :param ram: Количество оперативной памяти
        :param gpu: Название видеокарты
        """
        self.cpu = cpu
        self.ram = ram
        self.gpu = gpu

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, new_cpu: str) -> None:
        """Установка нового процессора."""
        if not isinstance(new_cpu, str):
            raise TypeError("Название процессора должно быть типа str")
        self._cpu = new_cpu

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, new_ram: int) -> None:
        """Установка новой оперативной памяти."""
        if not isinstance(new_ram, int):
            raise TypeError("Объем оперативной памяти должен быть типа int")
        if new_ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом")
        self._ram = new_ram

    @property
    def gpu(self):
        return self._gpu

    @gpu.setter
    def gpu(self, new_gpu: Union[str, None]) -> None:
        """Установка новой видеокарты."""
        if not isinstance(new_gpu, Union[str, None]):
            raise TypeError("Название видеокарты должно быть типа str или None")
        self._gpu = new_gpu

    def __str__(self) -> str:
        return f'Это {self.__class__.__name__}. \n' \
               f'В нем установлены: процессор - {self._cpu}, видеокарта - {self._gpu} и {self._ram} Гб ОЗУ.'

    def __repr__(self):
        return f'{self.__class__.__name__}(cpu = {self._cpu!r}, ram = {self._ram!r}, gpu = {self._gpu!r})'


class Laptop(Computer):
    def __init__(self, cpu: str, ram: int, gpu: Union[str, None], mouse):
        """
        Создание объекта "ноутбук"
        :param cpu: Название ЦП
        :param ram: Количество ОЗУ
        :param gpu: Название ГПУ
        :param mouse: Название мыши
        """
        super().__init__(cpu, ram, gpu)
        self.mouse = mouse

    def __repr__(self):
        return f'{self.__class__.__name__}(cpu = {self._cpu!r}, ram = {self._ram!r}, gpu = {self._gpu!r}, ' \
               f'mouse = {self.mouse!r})'


class TableComputer(Computer):
    def __init__(self, cpu: str, ram: int, gpu: Union[str, None], mouse: Union, keyboard: str, monitor: str):
        """
        Создание объекта настольный компьютер
        :param cpu: Название ЦП
        :param ram: Количество ОЗУ
        :param gpu: Название ГПУ
        :param mouse: Название мыши
        :param keyboard: Название клавиатуры
        :param monitor: Название монитора
        """
        super().__init__(cpu, ram, gpu)
        self.mouse = mouse
        self.keyboard = keyboard
        self.monitor = monitor

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, new_mouse: str) -> None:
        if not isinstance(new_mouse, str):
            raise TypeError("Вставьте мыш, чтобы взаимодействовать с компьютером")
        self._mouse = new_mouse

    @property
    def keyboard(self):
        return self._keyboard

    @keyboard.setter
    def keyboard(self, new_keayboard: str) -> None:
        if not isinstance(new_keayboard, str):
            raise TypeError("Вставьте клавиатуру, чтобы взаимодействовать с компьютером")
        self._keyboard = new_keayboard

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, new_monitor: str) -> None:
        if not isinstance(new_monitor, str):
            raise TypeError("Здесь должны быть ошибка, но вы её все равно не увидите")
        self._monitor = new_monitor

    def __repr__(self):
        return f'{self.__class__.__name__}(cpu = {self._cpu!r}, ram = {self._ram!r}, gpu = {self._gpu!r}, ' \
               f'mouse = {self._mouse!r}, keyboard = {self._keyboard!r}, monitor = {self._monitor!r})'


if __name__ == "__main__":

    test_pc = TableComputer("Xeon E5 2666v3", 16, "GTX660", 'Abyssus', 'K500', 'Mi')
    print(test_pc)
    print(repr(test_pc))
