from bookstore.printer.book_store_printer import BookStorePrinter
from bookstore.utils.facade.facade_constants import SEPARATOR, QUIT_MESSAGE


class ConsoleBookStorePrinter(BookStorePrinter):
    def print(self, content:str) -> None:
        print(content)
    def print_separator(self) -> None:
        print(SEPARATOR)
    def print_quit_option(self) -> None:
        print(SEPARATOR, QUIT_MESSAGE, SEPARATOR, sep="\n")