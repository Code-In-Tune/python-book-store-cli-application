from dataclasses import dataclass


@dataclass(frozen=True)
class InputField:
    field : str
    value : str
