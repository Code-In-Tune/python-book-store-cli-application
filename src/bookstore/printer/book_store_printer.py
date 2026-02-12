from typing import Protocol


class BookStorePrinter(Protocol):
    def print(self, content:str) -> None:
        ...
    def print_separator(self) -> None:
        ...
    def print_quit_option(self) -> None:
        ...