import re
from rest_framework.exceptions import ValidationError


def validate_plate_format(value):
    if not re.findall('^[A-Z]{3}[-][0-9]{3}$', value):
       raise ValidationError("The plate must follow the format ABC-123 ", code='wrong_format')