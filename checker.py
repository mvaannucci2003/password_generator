import string
import re
from collections import Counter
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
        pass_length = 5
    if 10 <= pass_length < 15:
        pass_length = 10
    if 15 <= pass_length < 20:
        pass_length = 15
    if 20 <= pass_length < 25:
        pass_length = 20
    if pass_length >= 25:
        pass_length = 25

    return pass_length



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
    score = 0
    dup = Counter(password)
    SYMBOL_CHARS = string.punctuation

    if re.findall(r"(.)\1", password):
        score -= 5

    if not any(c.islower() for c in password):
        score -= 5
    if not any(c.isupper() for c in password):
        score -= 5
    if not any(c.isdigit() for c in password):
        score -= 5
    if not any(c in SYMBOL_CHARS for c in password):
        score -= 5

    if [c for c, cnt in dup.items() if cnt > 1]:
        score -= 5

    return score





def check_strength(password: str) -> int:
    """
    Analyze password strength and return comprehensive results.

    :param password: Description
    :type password: str
    :return: Description
    :rtype: int
    """
    strength = dict(
        score = 0,
        rating = ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong'],
        length = 0,
        has_lower = True,
        has_upper = True,
        has_numbers = True,
        has_symbols = True
    )

    if calculate_length_score(password):
        pass
        # TODO Calculate your functions by putting them in the sum function for the accumlated score
        # TODO Determine the string rating based on the resulted score similar idea to the bool range check.
        # TODO Check character types by again reusing the logic from check_variety
        # TODO Return your DICT and complete the function.



if __name__ == "__main__":

    print(calculate_length_score(password="password123"))

    print(calculate_variety_score(password="passwor2"))

    print(calculate_pattern_penalty(password="Fasonhs1@m"))

    # result = check_strength("password")
    # print(f"Password: password")
    # print(f"Score: {result['score']}")
    # print(f"Rating: {result['rating']}")

    # result = check_strength("P@ssw0rd!2024")
    # print(f"\nPassword: P@ssw0rd!2024")
    # print(f"Score: {result['score']}")
    # print(f"Rating: {result['rating']}")
