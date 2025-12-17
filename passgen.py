import string
import secrets

LOWERCASE_CHARS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER_CHARS = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
SYMBOL_CHARS = "! @ # $ % ^ & * ( ) _ + | ; : < > , . / ?`~[]=-"


def validate_params(
    length: int,
    use_lowercase: bool,
    use_uppercase: bool,
    use_numbers: bool,
    use_symbols: bool,
) -> bool:
    """Validate password generation parameters"""

    if 8 <= length <= 128 and (
        use_lowercase or use_uppercase or use_numbers or use_symbols
    ):
        return True

    else:
        raise TypeError(
            f"{length} must be at least 8 numbers or a maximum of 128. Also, need at least one param to be True."
        )


def build_char_pool(
    use_lowercase: bool, use_uppercase: bool, use_numbers: bool, use_symbols: bool
) -> str:
    """build a string based on user preference."""
    use_lowercase = LOWERCASE_CHARS
    use_uppercase = UPPERCASE_CHARS
    use_numbers = NUMBER_CHARS
    use_symbols = SYMBOL_CHARS

    chars = use_uppercase or use_lowercase
    nums_symbols = use_numbers or use_symbols

    return chars or nums_symbols


def generate_password(
    length: int = 16,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str | None:
    """Generate a cryptographically secure random password."""
    pass


if __name__ == "__main__":
    print(
        build_char_pool(
            use_lowercase=False,
            use_numbers=False,
            use_symbols=False,
            use_uppercase=True,
        )
    )
