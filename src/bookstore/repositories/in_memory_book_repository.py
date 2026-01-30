from typing import Optional, Iterable, MutableMapping

from bookstore.model.book.book_record import BookRecord
from bookstore.repositories.book_repository import BookRepository


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books: MutableMapping[int, BookRecord] = dict()
        self.book_id_sequence : int = 0

    def get(self, book_id : int) -> Optional[BookRecord]:
        return self.books.get(book_id)

    def find_all(self) -> Iterable[BookRecord]:
        return self.books.values()

    def save(self, book: BookRecord) -> BookRecord:
        if book.book_id is not None:
            book.book_id = self.book_id_sequence
            self.book_id_sequence += 1
        self.books[book.book_id] = book
        return book

    def delete(self, book_id: int) -> None:
        self.books.pop(book_id)

    def find_all_by_title(self, title : str) -> Iterable[BookRecord]:
        case_fold_title = title.casefold()
        return [book for book in self.books.values() if case_fold_title in book.title.casefold()]

    def find_all_by_author(self, author : str) -> Iterable[BookRecord]:
        case_fold_author = author.casefold()
        return [book for book in self.books.values() if case_fold_author in book.author.casefold()]

