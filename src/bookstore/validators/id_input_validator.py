from bookstore.exception.validation_error import ValidationError
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator


class IdInputValidator(Validator[InputField]):
    def validate(self, data : InputField) -> None:
        value : str = data.value
        field : str = data.field
        if not value.isdigit():
            raise ValidationError(f"Invalid value for field '{field}': {value}", field =  field)
