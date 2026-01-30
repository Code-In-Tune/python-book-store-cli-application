from bookstore.exception.ValidationError import ValidationError
from bookstore.utils.input.input_validators_constants import ISBN_PATTERN
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator
import re

class IsbnInputValidator(Validator[InputField]):
    def validate(self, data : InputField) -> None:
        field : str = data.field
        value : str = data.value
        if not re.match(ISBN_PATTERN, field):
            raise ValidationError(f"Field '{field}' is not a valid ISBN: {value}", field =  field)