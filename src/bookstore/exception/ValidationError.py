class ValidationError(Exception):
    """Raised when validation fails"""
    def __init__(self, message: str, field: str) -> None:
        Exception.__init__(self, message)
        self.field = field