from typing import Protocol, TypeVar

T = TypeVar('T')

class Validator(Protocol[T]):
    def validate(self, data : T) -> None:
        ...