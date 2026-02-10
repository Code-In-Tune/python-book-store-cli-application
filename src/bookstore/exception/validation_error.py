"""
Raised when validation fails
"""
class ValidationError(Exception):
    def __init__(self, message: str, field: str) -> None:
        Exception.__init__(self, message)
        self.field = field