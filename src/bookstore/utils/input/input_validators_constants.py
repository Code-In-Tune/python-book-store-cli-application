import re
from re import Pattern

ISBN_PATTERN : Pattern[str] = re.compile("^(?:[0-9]{9}[0-9X]|97[89][0-9]{10})$")
NAME_PATTERN : Pattern[str] = re.compile("^[a-zA-Z .]+$")
PRICE_PATTERN : Pattern[str] = re.compile("^([0-9]+)\\.([0-9]{2})$")
