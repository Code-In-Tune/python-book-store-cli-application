from decimal import Decimal

from bookstore.dto.book.add_book_request_dto import AddBookRequestDTO
from bookstore.dto.book.add_book_response_dto import AddBookResponseDto
from bookstore.dto.book.get_book_response_dto import GetBookResponseDto
from bookstore.dto.book.update_book_by_id_request_dto import UpdateBookByIdRequestDTO
from bookstore.mapper.book.book_mapper import BookMapper
from bookstore.model.book.book_record import BookRecord
from bookstore.model.book.enums.availability import Availability


class BookRecordMapper(BookMapper):

    def to_entity(self, request: AddBookRequestDTO) -> BookRecord:
        quantity = int(request.quantity)
        price = Decimal(request.price)
        return BookRecord(
            title=request.title,
            author=request.author,
            publisher=request.publisher,
            quantity=quantity,
            isbn=request.isbn,
            price=price,
            availability=Availability.IN_STOCK
        )

    def to_dto(self, book : BookRecord) -> AddBookResponseDto:
        book_id = str(book.book_id)
        quantity = str(book.quantity)
        price = str(book.price)
        return AddBookResponseDto(
            book_id=book_id,
            title=book.title,
            author=book.author,
            publisher=book.publisher,
            quantity=quantity,
            isbn=book.isbn,
            price=price,
            availability=book.availability.name
        )

    def to_get_dto(self, book : BookRecord) -> GetBookResponseDto:
        book_id = str(book.book_id)
        quantity = str(book.quantity)
        price = str(book.price)
        return GetBookResponseDto(
            book_id=book_id,
            title=book.title,
            author=book.author,
            publisher=book.publisher,
            quantity=quantity,
            isbn=book.isbn,
            price=price,
            availability=book.availability.name
        )

    def update_entity(self, book : BookRecord, request : UpdateBookByIdRequestDTO) -> None:
        book.quantity = int(request.quantity)
        book.title = request.title
        book.author = request.author
        book.publisher = request.publisher
        book.isbn = request.isbn
        book.price = Decimal(request.price)