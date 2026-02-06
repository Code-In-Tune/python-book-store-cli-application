import dataclasses


@dataclasses.dataclass(frozen=True)
class GetBooksByAuthorRequestDto:
    title : str