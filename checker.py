import string

# Total score: 0-100 points
# Length score: 0-25 points
# Variety score: 0-60 points (15 points per character type)
# Pattern penalty: negative points for weak patterns


def calculate_length_score(password: str) -> int:
    """
    Calculate score based on password strength.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    pass_length = len(password)

    if 5 <= pass_length < 10:
        return 5
    if 10 <= pass_length < 15:
        return 10
    if 15 <= pass_length < 20:
        return 15
    if 20 <= pass_length < 25:
        return 20
    if pass_length >= 25:
        return 25


# Scoring rules:
# - Award 15 points if password contains lowercase letters
# - Award 15 points if password contains uppercase letters
# - Award 15 points if password contains numbers
# - Award 15 points if password contains symbols
# - Maximum possible: 60 points
def calculate_variety_score(password: str) -> int:
    """
    Calculate score based on character type diversity.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    SYMBOL_CHARS = string.punctuation
    score = 0

    if any(c.islower() for c in password):
        score += 15
    if any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15
    if any(c in SYMBOL_CHARS for c in password):
        score += 15

    return score


def calculate_pattern_penalty(password: str) -> int:
    """
    Detect weak patterns and calculate penalty.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    pass


def check_strength(password: str) -> int:
    """
    Analyze password strength and return comprehensive results.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    pass


if __name__ == "__main__":

    print(calculate_length_score(password="password"))

    print(calculate_variety_score(password="password"))

    # result = check_strength("password")
    # print(f"Password: password")
    # print(f"Score: {result['score']}")
    # print(f"Rating: {result['rating']}")

    # result = check_strength("P@ssw0rd!2024")
    # print(f"\nPassword: P@ssw0rd!2024")
    # print(f"Score: {result['score']}")
    # print(f"Rating: {result['rating']}")
