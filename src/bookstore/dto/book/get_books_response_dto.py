import dataclasses
from typing import Iterable

from bookstore.dto.book.get_book_by_id_request_dto import GetBookByIdRequestDTO

@dataclasses.dataclass(frozen=True)
class GetBooksResponseDto:
    books: Iterable[GetBookByIdRequestDTO]