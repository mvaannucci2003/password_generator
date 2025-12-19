from generator import generate_password

"""Total score: 0-100 points
- Length score: 0-25 points
- Variety score: 0-60 points (15 points per character type)
- Pattern penalty: negative points for weak patterns"""


def calculate_length_score(password: str) -> int:
    """
    Calculate score based on password strength.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    pass_length = len(generate_password(60))

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


def calculate_variety_score(password: str) -> int:
    pass


def calculate_pattern_penalty(password: str) -> int:
    pass


def check_strength(password: str) -> int:
    pass


if __name__ == "__main__":

    pass
