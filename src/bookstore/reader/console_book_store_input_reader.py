from bookstore.exception.operation_aborted_error import OperationAbortedError
from bookstore.reader.book_store_input_reader import BookStoreInputReader
from bookstore.utils.facade.facade_constants import QUIT_OPTION


class ConsoleBookStoreInputReader(BookStoreInputReader):
    def read_next_line_with_quit_option(self) -> str:
        option : str = input().strip()
        if option == QUIT_OPTION:
            raise OperationAbortedError("Operation Aborted")
        return option

    def read_next_line(self) -> str:
        return input().strip()