import dataclasses


@dataclasses.dataclass(frozen=True)
class GetBookByIdRequestDTO:
    book_id   : str