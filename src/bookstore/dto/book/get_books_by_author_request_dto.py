import dataclasses


@dataclasses.dataclass(frozen=True)
class GetBooksByAuthorRequestDto:
    author : str