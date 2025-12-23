import argparse
import sys
from generator import generate_password
from checker import check_strength

def main():
    """
    Main function for password generator.

    This function:
    1. Creates an ArgumentParser
    2. Adds subparser for 'generate' and 'check' commands
    3. Configures arguments for each subcommand
    4. Parses command-line arguments
    5. Calls appropriate handler based on command
    6. Handles errors gracefully
    """

parser = argparse.ArgumentParser(
    description='Password Generator and Strength Checker',
    epilog='Use "passgen.py <command> --help" for command-specific help'
)

# Create subparsers for commands
subparser = parser.add_subparsers(dest='command', help='Available commands')

# TODO configure generate subparser
#add arguments here

#TODO configure check subparser
#add arguments here

args = parser.parse_args()

#Handlers
if args.command == 'generate':
    #Call handle_generate(args)
    pass
elif args.command == 'check':
    #Call handle_check(args)
    pass
else:
    parser.print_help()
    sys.exit(1)



if __name__ == '__main__':
    main()
