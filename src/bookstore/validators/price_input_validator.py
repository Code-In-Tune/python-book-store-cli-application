import re

from bookstore.exception.validation_error import ValidationError
from bookstore.utils.input.input_validators_constants import PRICE_PATTERN
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator


class PriceInputValidator(Validator[InputField]):
    def validate(self, data : InputField) -> None:
        value : str = data.value
        field : str = data.field
        if not re.match(PRICE_PATTERN, value):
            raise ValidationError(f"Field '{field}' is not a valid price: {value}", field = field)