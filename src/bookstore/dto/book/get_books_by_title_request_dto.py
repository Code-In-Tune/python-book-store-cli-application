import dataclasses


@dataclasses.dataclass(frozen=True)
class GetBooksByTitleRequestDto:
    title : str