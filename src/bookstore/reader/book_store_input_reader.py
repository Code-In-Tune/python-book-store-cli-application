from typing import Protocol


class BookStoreInputReader(Protocol):

    def read_next_line_with_quit_option(self) -> str:
        ...
    def read_next_line(self) -> str:
        ...