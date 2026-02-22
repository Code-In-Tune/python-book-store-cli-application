from bookstore.dto.book.add_book_request_dto import AddBookRequestDTO
from bookstore.dto.book.get_book_by_id_request_dto import GetBookByIdRequestDTO
from bookstore.printer.book_store_printer import BookStorePrinter
from bookstore.reader.book_store_input_reader import BookStoreInputReader
from bookstore.service.book_input_service import BookInputService
from bookstore.utils.input.book_input_service_constants import INSERT_BOOK_TITLE_MESSAGE, INSERT_BOOK_AUTHOR_MESSAGE, \
    INSERT_BOOK_ISBN_MESSAGE, INSERT_BOOK_QUANTITY_MESSAGE, INSERT_BOOK_PRICE_MESSAGE, INSERT_BOOK_PUBLISHER_MESSAGE, \
    INSERT_BOOK_ID_MESSAGE
from bookstore.utils.input.input_field_constants import TITLE_FIELD, AUTHOR_FIELD, ISBN_FIELD, QUANTITY_FIELD, \
    PRICE_FIELD, PUBLISHER_FIELD, ID_FIELD
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator


class ConsoleBookInputService(BookInputService):
    def __init__(self,
                 book_input_reader : BookStoreInputReader,
                 book_store_printer : BookStorePrinter,
                 input_name_validator : Validator,
                 input_isbn_validator : Validator,
                 input_quantity_validator : Validator,
                 input_price_validator : Validator,
                 input_id_validator : Validator,
                 ) -> None:
        self.book_input_reader = book_input_reader
        self.book_store_printer = book_store_printer
        self.input_name_validator = input_name_validator
        self.input_isbn_validator = input_isbn_validator
        self.input_quantity_validator = input_quantity_validator
        self.input_price_validator = input_price_validator
        self.input_id_validator = input_id_validator


    def build_add_book_request_dto(self) -> AddBookRequestDTO:
        self.book_store_printer.print(INSERT_BOOK_TITLE_MESSAGE)
        self.book_store_printer.print_quit_option()

        title : str = self.book_input_reader.read_next_line_with_quit_option()

        title_field : InputField = InputField(field=TITLE_FIELD, value=title)

        self.input_name_validator.validate(title_field)

        self.book_store_printer.print(INSERT_BOOK_AUTHOR_MESSAGE)
        self.book_store_printer.print_quit_option()

        author : str = self.book_input_reader.read_next_line_with_quit_option()

        author_field : InputField = InputField(field=AUTHOR_FIELD, value=author)

        self.input_name_validator.validate(author_field)

        self.book_store_printer.print(INSERT_BOOK_ISBN_MESSAGE)
        self.book_store_printer.print_quit_option()

        isbn : str = self.book_input_reader.read_next_line_with_quit_option()

        isbn_field : InputField = InputField(field=ISBN_FIELD, value=isbn)

        self.input_isbn_validator.validate(isbn_field)

        self.book_store_printer.print(INSERT_BOOK_QUANTITY_MESSAGE)
        self.book_store_printer.print_quit_option()

        quantity : str = self.book_input_reader.read_next_line_with_quit_option()

        quantity_field : InputField = InputField(field=QUANTITY_FIELD, value=quantity)

        self.input_quantity_validator.validate(quantity_field)

        self.book_store_printer.print(INSERT_BOOK_PRICE_MESSAGE)
        self.book_store_printer.print_quit_option()

        price : str = self.book_input_reader.read_next_line_with_quit_option()

        price_field : InputField = InputField(field=PRICE_FIELD, value=price)

        self.input_price_validator.validate(price_field)

        self.book_store_printer.print(INSERT_BOOK_PUBLISHER_MESSAGE)
        self.book_store_printer.print_quit_option()

        publisher : str = self.book_input_reader.read_next_line_with_quit_option()

        publisher_field : InputField = InputField(field=PUBLISHER_FIELD, value=publisher)

        self.input_name_validator.validate(publisher_field)

        return AddBookRequestDTO(
            title= title,
            author= author,
            isbn= isbn,
            quantity= quantity,
            price= price,
            publisher= publisher,
        )

    def build_get_book_by_id_request_dto(self) -> GetBookByIdRequestDTO:
        self.book_store_printer.print(INSERT_BOOK_ID_MESSAGE)
        self.book_store_printer.print_quit_option()

        id : str = self.book_input_reader.read_next_line_with_quit_option()

        input_id : InputField = InputField(field=ID_FIELD, value=id)

        self.input_id_validator.validate(input_id)

        return GetBookByIdRequestDTO(
            book_id= id
        )