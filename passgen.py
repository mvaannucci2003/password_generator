import string
import secrets

LOWERCASE_CHARS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER_CHARS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
SYMBOL_CHARS = "! @ # $ % ^ & * ( ) _ + | ; : < > , . / ?`~[]=-"


def validate_params(
    length: int,
    use_lowercase: bool,
    use_uppercase: bool,
    use_numbers: bool,
    use_symbols: bool,
) -> bool:
    """Validate password generation parameters"""

    pass
