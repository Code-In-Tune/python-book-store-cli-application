from bookstore.exception.ValidationError import ValidationError
from bookstore.validators.field.input_field import InputField
from bookstore.validators.validator import Validator


class QuantityInputValidator(Validator[InputField]):
    def validate(self, data : InputField) -> None:
        value : str = data.value
        field : str = data.field
        if not value.isdigit() or int(value) == 0:
            raise ValidationError(f"Field '{field}' is not a valid quantity: {value}", field = field)