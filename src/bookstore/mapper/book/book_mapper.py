from typing import Protocol

from bookstore.dto.book.add_book_request_dto import AddBookRequestDTO
from bookstore.dto.book.add_book_response_dto import AddBookResponseDto
from bookstore.dto.book.get_book_response_dto import GetBookResponseDto
from bookstore.dto.book.update_book_by_id_request_dto import UpdateBookByIdRequestDTO
from bookstore.model.book.book_record import BookRecord


class BookMapper(Protocol):
    def to_entity(self, request: AddBookRequestDTO) -> BookRecord:
        ...
    def to_dto(self, book : BookRecord) -> AddBookResponseDto:
        ...
    def to_get_dto(self, book : BookRecord) -> GetBookResponseDto:
        ...
    def update_entity(self, book : BookRecord, request : UpdateBookByIdRequestDTO) -> None:
        ...
