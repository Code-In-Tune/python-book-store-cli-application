from bookstore.exception.ValidationError import ValidationError
from bookstore.utils.input.input_validators_constants import NAME_PATTERN
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator
import re

class NameInputValidator(Validator[InputField]):
    def validate(self, data: InputField) -> None:
        value : str = data.value
        field : str = data.field
        if not re.match(NAME_PATTERN, value):
            raise ValidationError(f"Field '{field}':{value} is not a valid name", field = field)
