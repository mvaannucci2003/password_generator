import argparse
import sys
from generator import generate_password
from checker import check_strength


def main():
    """
    Main function for password generator.
    """

    parser = argparse.ArgumentParser(
        description="Password Generator and Strength Checker",
        epilog='Use "passgen.py <command> --help" for command-specific help',
    )

    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    gen_parser = subparsers.add_parser("generate", help="Generate secure passwords")
    gen_parser.add_argument(
        "--length", type=int, default=16, help="Specifies desired length of password"
    )
    gen_parser.add_argument(
        "--no-lowercase", action="store_true", help="Excludes lowercase in generation"
    )
    gen_parser.add_argument(
        "--no-uppercase", action="store_true", help="Excludes uppercase in generation"
    )
    gen_parser.add_argument(
        "--no-numbers", action="store_true", help="Excludes numbers in generation"
    )
    gen_parser.add_argument(
        "--no-symbols", action="store_true", help="Excludes symbols in generation"
    )
    gen_parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Amount of passwords that should be generated",
    )

    check_parser = subparsers.add_parser("check", help="Check password strength")
    check_parser.add_argument("password")

    args = parser.parse_args()
    # Handlers
    if args.command == "generate":
        handle_generate(args)
    elif args.command == "check":
        handle_check(args)
        pass
    else:
        parser.print_help()
        sys.exit(1)


def handle_generate(args):
    """
    Handle the 'generate' command.

    Args:
    args: Parsed command-line arguments from argparse

    Output format:
    If count=1: "Generated password: {password}"
    If count>1: "Password 1: {password}\nPassword 2: {password}\n..."
    """
    length = args.length

    lowcase = not args.no_lowercase

    upcase = not args.no_uppercase

    nums = not args.no_numbers

    syms = not args.no_symbols

    password = generate_password(
        length=length,
        use_lowercase=lowcase,
        use_uppercase=upcase,
        use_numbers=nums,
        use_symbols=syms,
    )
    if args.count == 1:
        print(f"Generated password: {password}")
    elif args.count > 1:

        for i in range(args.count):

            password = generate_password()

            print(f"Generated password: {password}")


def handle_check(args):
    """
    Handle the 'check' command.

    :param args: Parsed command-line arguments from argparse
    """

    secret = args.password
    result = check_strength(password=secret)

    print(f"\nPassword: {secret}")
    print(f"Score: {result['score']}")
    print(f"Rating: {result['rating']}")


if __name__ == "__main__":
    main()
