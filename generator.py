import secrets

LOWERCASE_CHARS = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER_CHARS = "0123456789"
SYMBOL_CHARS = "!@#$%^&*()_+|;:<>,./?`~[]=-"


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
        return False


def build_char_pool(
    use_lowercase: bool, use_uppercase: bool, use_numbers: bool, use_symbols: bool
) -> str:
    """build a string based on user preference."""
    pool = ""

    if use_lowercase:
        pool = pool + LOWERCASE_CHARS
    if use_uppercase:
        pool = pool + UPPERCASE_CHARS
    if use_numbers:
        pool = pool + NUMBER_CHARS
    if use_symbols:
        pool = pool + SYMBOL_CHARS

    return pool


def generate_password(
    length: int = 16,
    use_lowercase: bool = True,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str | None:
    """Generate a cryptographically secure random password."""

    if not validate_params(
        length, use_lowercase, use_uppercase, use_numbers, use_symbols
    ):
        return None
    chars = build_char_pool(use_lowercase, use_uppercase, use_numbers, use_symbols)

    password = "".join(secrets.choice(chars) for _ in range(length))

    return password


if __name__ == "__main__":
    print(generate_password())
    print(generate_password(length=24, use_symbols=False))
    print(generate_password(length=5))
