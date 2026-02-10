from typing import Protocol

from bookstore.dto.book.add_book_request_dto import AddBookRequestDTO
from bookstore.dto.book.get_book_by_id_request_dto import GetBookByIdRequestDTO
from bookstore.dto.book.get_books_by_author_request_dto import GetBooksByAuthorRequestDto
from bookstore.dto.book.get_books_by_title_request_dto import GetBooksByTitleRequestDto
from bookstore.dto.book.update_book_by_id_request_dto import UpdateBookByIdRequestDTO
from bookstore.dto.book.update_book_quantity_by_id_request_dto import UpdateBookQuantityByIdRequestDTO


class BookInputService(Protocol):
    def build_add_book_request_dto(self) -> AddBookRequestDTO:
        ...
    def build_get_book_by_id_request_dto(self) -> GetBookByIdRequestDTO:
        ...
    def build_get_books_by_author_request_dto(self) -> GetBooksByAuthorRequestDto:
        ...
    def build_get_books_by_title_request_dto(self) -> GetBooksByTitleRequestDto:
        ...
    def build_update_book_by_id_request_dto(self) -> UpdateBookByIdRequestDTO:
        ...
    def build_update_book_quantity_request_dto(self) -> UpdateBookQuantityByIdRequestDTO:
        ...
