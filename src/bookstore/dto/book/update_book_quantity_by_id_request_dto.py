import dataclasses


@dataclasses.dataclass(frozen=True)
class UpdateBookQuantityByIdRequestDTO:
    book_id  : str
    quantity : str