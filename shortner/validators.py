from django.core.validators import URLValidator
from django.core.validators import ValidationError


def validate_url(value):
    url_validator = URLValidator()
    reg_value = value
    if "http" in reg_value:
        new_value = reg_value

    else:
        new_value = "http://" + value
    try:
        url_validator(new_value)
    except:
        raise ValidationError("Invalid URL for this field")
    return value


def validate_dot_com(value):
    if ".com" not in value:
        raise ValidationError("This is not valid because of no .com")
    return value
