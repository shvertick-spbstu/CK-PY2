class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. В книге {self._pages} страниц."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration (self, new_duration: float) -> None:
        """Устанавливает длительность книги."""
        if not isinstance(new_duration, (float, int)):
            raise TypeError("Длительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Длительность книги должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Дительность книги {self._duration} минут."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"


if __name__ == "__main__":

    test_book = Book("НАВЗАНИЕ", "АВТОР")
    test_paper_book = PaperBook("НАВЗАНИЕ", "АВТОР", 20)
    test_audi_book = AudioBook("НАВЗАНИЕ", "АВТОР", 20)
    print(test_paper_book)
