from typing import List

from pydantic import BaseModel

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book(BaseModel):
    id_: int
    name: str
    pages: int

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"

class Library(BaseModel):
    books: List[Book] = []

    def __init__(self, books = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        if self.books ==[]:
            raise ValueError("Библиотека пустая")
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i
        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
#Task1
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)
    print(list_books)
#Task 2
    empty_library = Library()
    print(empty_library.get_next_book_id())
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))
