# Password Generator and Strength Checker - Project Specification

**Estimated Time:** 4-6 hours  
**Difficulty:** Intermediate  
**Learning Focus:** Module organization, function design, CLI development, cryptographic security

---

## Project Overview

Build a command-line tool that generates cryptographically secure passwords and analyzes password strength. This project will teach you how to organize code across multiple modules, design clean function interfaces, and build user-friendly command-line tools.

---

## Project Structure

```
password-tool/
├── passgen.py          # Main entry point - handles CLI and user interaction
├── generator.py        # Password generation logic - pure functions, no I/O
├── checker.py          # Strength analysis logic - pure functions, no I/O
└── README.md           # Project documentation
```

**Architectural principle:** Separate user interface (CLI) from business logic (generation/checking). This allows you to:
- Test logic functions independently
- Change CLI without touching core logic
- Reuse logic functions in other contexts (web app, GUI, etc.)
- Follow single-responsibility principle

**Reference codebases to study AFTER you finish:**
- Simple CLI structure: https://github.com/pallets/click
- Python stdlib organization: https://github.com/python/cpython/tree/main/Lib
- Real password tool: https://github.com/pypa/pip (complex, but good patterns)

---

## Part 1: Password Generator Module (generator.py)

This module contains pure logic functions for password generation. No user interaction, no print statements - just functions that take inputs and return outputs.

### Required Imports
```python
import string
import secrets
```

### Constants You'll Need

Define four character set constants at the module level (after imports, before functions):
- `LOWERCASE_CHARS` - all lowercase letters a-z
- `UPPERCASE_CHARS` - all uppercase letters A-Z
- `NUMBER_CHARS` - all digits 0-9
- `SYMBOL_CHARS` - common symbols for passwords

**You figure out:** How to get these character sets (hint: explore the `string` module, or define your own strings)

---

### Function 1: Parameter Validation

```python
def validate_params(length: int, use_lowercase: bool, use_uppercase: bool, 
                   use_numbers: bool, use_symbols: bool) -> bool:
    """
    Validate password generation parameters.
    
    Args:
        length: Desired password length
        use_lowercase: Whether to include lowercase letters
        use_uppercase: Whether to include uppercase letters
        use_numbers: Whether to include numbers
        use_symbols: Whether to include symbols
    
    Returns:
        True if parameters are valid, False otherwise
    
    Validation rules:
        - length must be between 8 and 128 (inclusive)
        - At least one character type must be True
    """
    pass
```

**You figure out:** How to check these two conditions and return the appropriate boolean.

---

### Function 2: Character Pool Builder

```python
def build_char_pool(use_lowercase: bool, use_uppercase: bool, 
                   use_numbers: bool, use_symbols: bool) -> str:
    """
    Build a string containing all available characters based on user preferences.
    
    Args:
        use_lowercase: Whether to include lowercase letters
        use_uppercase: Whether to include uppercase letters
        use_numbers: Whether to include numbers
        use_symbols: Whether to include symbols
    
    Returns:
        A string containing all characters that can be used in the password
    
    Example:
        If use_lowercase=True and use_numbers=True, but others are False,
        return a string containing 'a-z' and '0-9'
    """
    pass
```

**You figure out:** How to conditionally build a string by combining the character set constants.

---

### Function 3: Password Generator

```python
def generate_password(length: int = 16, use_lowercase: bool = True, 
                     use_uppercase: bool = True, use_numbers: bool = True,
                     use_symbols: bool = True) -> str | None:
    """
    Generate a cryptographically secure random password.
    
    Args:
        length: Password length (default: 16)
        use_lowercase: Include lowercase letters (default: True)
        use_uppercase: Include uppercase letters (default: True)
        use_numbers: Include numbers (default: True)
        use_symbols: Include symbols (default: True)
    
    Returns:
        Generated password string, or None if parameters are invalid
    
    Implementation requirements:
        - Must use secrets.choice(), NOT random.choice()
        - Must call validate_params() first
        - Must call build_char_pool() to get available characters
        - Must build password by selecting random characters
    """
    pass
```

**You figure out:** 
- How to call your validation and pool-building functions
- How to use `secrets.choice()` to pick random characters
- How to build a string of the specified length
- How to return None vs. a password string

**Testing your generator:**
At the bottom of generator.py, add:
```python
if __name__ == '__main__':
    # Test your functions here
    print(generate_password())
    print(generate_password(length=24, use_symbols=False))
    print(generate_password(length=5))  # Should return None
```

---

## Part 2: Password Strength Checker Module (checker.py)

This module analyzes password strength. Like generator.py, it contains pure logic functions with no user interaction.

### Scoring System Overview

Total score: 0-100 points
- Length score: 0-25 points
- Variety score: 0-60 points (15 points per character type)
- Pattern penalty: negative points for weak patterns

Strength ratings based on total score:
- You decide the thresholds for: Very Weak, Weak, Medium, Strong, Very Strong

---

### Function 1: Length Scoring

```python
def calculate_length_score(password: str) -> int:
    """
    Calculate score based on password length.
    
    Args:
        password: The password to score
    
    Returns:
        Score from 0-25 based on length
    
    Scoring guidelines:
        - Longer passwords should score higher
        - Minimum 8 characters to get any points
        - Maximum 25 points for very long passwords
        - You decide the specific length tiers
    """
    pass
```

**You figure out:** What length ranges deserve what scores. Be reasonable - a 12 character password shouldn't max out, but a 30 character one should.

---

### Function 2: Character Variety Scoring

```python
def calculate_variety_score(password: str) -> int:
    """
    Calculate score based on character type diversity.
    
    Args:
        password: The password to score
    
    Returns:
        Score from 0-60 based on character variety
    
    Scoring rules:
        - Award 15 points if password contains lowercase letters
        - Award 15 points if password contains uppercase letters
        - Award 15 points if password contains numbers
        - Award 15 points if password contains symbols
        - Maximum possible: 60 points
    
    Hint: Use any() with generator expressions to check for character types
    Example: any(c.islower() for c in password) checks for lowercase
    """
    pass
```

**You figure out:** 
- How to detect if password contains each character type
- How to add up the points
- What counts as a "symbol" (probably check against your SYMBOL_CHARS constant)

---

### Function 3: Pattern Detection and Penalties

```python
def calculate_pattern_penalty(password: str) -> int:
    """
    Detect weak patterns and calculate penalty.
    
    Args:
        password: The password to analyze
    
    Returns:
        Negative integer (or 0) representing penalty points
    
    Patterns to detect and penalize:
        - Sequential characters (abc, 123, xyz) - you decide penalty
        - Repeated characters (aaa, 111, xxx) - you decide penalty
        - Only one character type used - you decide penalty
    
    Note: Return value should be 0 or negative (penalties subtract from score)
    
    Hints:
        - For sequential: check if any 3 consecutive chars have consecutive ASCII values
        - For repeated: check if any character appears 3+ times in a row
        - For single type: use your variety checking logic
    """
    pass
```

**You figure out:** 
- How to detect sequential characters (ASCII value math?)
- How to detect repeated characters (string iteration?)
- How severe each penalty should be
- How to return penalties as negative numbers

---

### Function 4: Main Strength Checker

```python
def check_strength(password: str) -> dict:
    """
    Analyze password strength and return comprehensive results.
    
    Args:
        password: The password to analyze
    
    Returns:
        Dictionary with the following keys:
            'score': int - total score (0-100)
            'rating': str - rating based on score (Very Weak/Weak/Medium/Strong/Very Strong)
            'length': int - password length
            'has_lowercase': bool - contains lowercase letters
            'has_uppercase': bool - contains uppercase letters
            'has_numbers': bool - contains numbers
            'has_symbols': bool - contains symbols
    
    Implementation:
        - Call calculate_length_score()
        - Call calculate_variety_score()
        - Call calculate_pattern_penalty()
        - Sum all scores (remember penalty is negative)
        - Determine rating based on total score
        - Detect character types (reuse logic from variety scoring)
        - Return dictionary with all required keys
    """
    pass
```

**You figure out:** 
- How to call the three scoring functions and combine results
- What score ranges map to what ratings
- How to detect character types for the boolean flags
- How to construct and return the dictionary

**Testing your checker:**
At the bottom of checker.py, add:
```python
if __name__ == '__main__':
    # Test your functions here
    result = check_strength("password")
    print(f"Password: password")
    print(f"Score: {result['score']}")
    print(f"Rating: {result['rating']}")
    
    result = check_strength("P@ssw0rd!2024")
    print(f"\nPassword: P@ssw0rd!2024")
    print(f"Score: {result['score']}")
    print(f"Rating: {result['rating']}")
```

---

## Part 3: Command-Line Interface (passgen.py)

This module provides the user interface. It imports functions from generator.py and checker.py, handles command-line arguments, and displays results.

### Required Imports
```python
import argparse
import sys
from generator import generate_password
from checker import check_strength
```

---

### Main Function Structure

```python
def main():
    """
    Main entry point for the CLI application.
    
    This function should:
        1. Create an ArgumentParser
        2. Add subparsers for 'generate' and 'check' commands
        3. Configure arguments for each subcommand
        4. Parse command-line arguments
        5. Call appropriate handler based on command
        6. Handle errors gracefully
    """
    # Create parser
    parser = argparse.ArgumentParser(
        description='Password Generator and Strength Checker',
        epilog='Use "passgen.py <command> --help" for command-specific help'
    )
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Configure 'generate' subparser
    # You'll add arguments here
    
    # Configure 'check' subparser
    # You'll add arguments here
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'generate':
        # Call handle_generate(args)
        pass
    elif args.command == 'check':
        # Call handle_check(args)
        pass
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
```

**You figure out:** How to fill in this skeleton with actual argparse configuration.

---

### Generate Command Configuration

Your 'generate' subparser needs these arguments:

```python
gen_parser = subparsers.add_parser('generate', help='Generate secure passwords')
# Add these arguments to gen_parser:
# --length (type=int, default=16, help text)
# --no-lowercase (action='store_true', help text)
# --no-uppercase (action='store_true', help text)
# --no-numbers (action='store_true', help text)
# --no-symbols (action='store_true', help text)
# --count (type=int, default=1, help text)
```

**You figure out:** The exact argparse syntax for adding these arguments.

---

### Check Command Configuration

Your 'check' subparser needs one positional argument:

```python
check_parser = subparsers.add_parser('check', help='Check password strength')
# Add this argument to check_parser:
# password (positional, help text)
```

**You figure out:** The exact argparse syntax for a positional argument.

---

### Generate Command Handler

```python
def handle_generate(args):
    """
    Handle the 'generate' command.
    
    Args:
        args: Parsed command-line arguments from argparse
    
    This function should:
        1. Convert --no-* flags to use_* booleans (invert them)
        2. Call generate_password() with appropriate parameters
        3. Handle None return (validation failure) with error message
        4. Generate args.count passwords
        5. Display results clearly
    
    Output format:
        If count=1: "Generated password: {password}"
        If count>1: "Password 1: {password}\nPassword 2: {password}\n..."
    """
    pass
```

**You figure out:** 
- How to convert `--no-lowercase` flag to `use_lowercase` boolean
- How to loop and generate multiple passwords
- How to format output appropriately
- How to handle errors (print message, sys.exit(1))

---

### Check Command Handler

```python
def handle_check(args):
    """
    Handle the 'check' command.
    
    Args:
        args: Parsed command-line arguments from argparse
    
    This function should:
        1. Call check_strength() with the password from args
        2. Extract results from returned dictionary
        3. Display comprehensive analysis
    
    Output format:
        Password: {password}
        Length: {length} characters
        Has lowercase: {Yes/No}
        Has uppercase: {Yes/No}
        Has numbers: {Yes/No}
        Has symbols: {Yes/No}
        Strength: {rating} ({score}/100)
    """
    pass
```

**You figure out:** 
- How to access the password from args
- How to convert boolean values to "Yes"/"No" strings
- How to format the multi-line output

---

## Error Handling Requirements

Your program should handle these error cases gracefully:

1. **Invalid length:** Print "Error: Password length must be between 8 and 128"
2. **No character types selected:** Print "Error: Must select at least one character type"
3. **No command provided:** Call `parser.print_help()`

**You figure out:** Where to add these checks and how to display errors.

---

## Testing Checklist

Test your program with these commands and verify the behavior:

```bash
# Basic generation
python passgen.py generate
# Should produce 16-character password with all types

# Custom length
python passgen.py generate --length 24
# Should produce 24-character password

# Exclude symbols
python passgen.py generate --no-symbols
# Should produce password without symbols

# Multiple passwords
python passgen.py generate --count 5
# Should produce 5 different passwords

# Error: length too short
python passgen.py generate --length 5
# Should print error message

# Error: no character types
python passgen.py generate --no-lowercase --no-uppercase --no-numbers --no-symbols
# Should print error message

# Check weak password
python passgen.py check "password"
# Should show Very Weak or Weak rating

# Check strong password
python passgen.py check "P@ssw0rd!2024"
# Should show Strong rating

# Help messages
python passgen.py --help
python passgen.py generate --help
python passgen.py check --help
```

---

## Documentation (README.md)

Create a README.md file with these sections:

1. **Project Title and Description** - What does this tool do?
2. **Features** - List of capabilities
3. **Usage** - How to run each command with examples
4. **Project Structure** - Brief explanation of each file
5. **Requirements** - Dependencies (none for this project, but mention Python 3.10+)

Keep it concise - aim for 30-50 lines total. Write it for someone who's never seen your code before.

---

## Development Workflow Suggestions

**Step 1: Build generator.py**
- Start with constants
- Write validate_params()
- Write build_char_pool()
- Write generate_password()
- Test each function as you go

**Step 2: Build checker.py**
- Write calculate_length_score()
- Write calculate_variety_score()
- Write calculate_pattern_penalty()
- Write check_strength()
- Test with known passwords

**Step 3: Build passgen.py**
- Set up argument parser structure
- Add arguments to subparsers
- Write handle_generate()
- Write handle_check()
- Test CLI with various inputs

**Step 4: Integration testing**
- Run all test cases from checklist
- Fix any edge cases you discover
- Add error handling where needed

**Step 5: Documentation**
- Write README.md
- Add docstrings if missing
- Add comments for complex logic

---

## Key Concepts You'll Learn

- **Module organization**: Separating concerns across files
- **Function design**: Clear inputs, outputs, single responsibility
- **CLI development**: Using argparse for professional command-line tools
- **Cryptographic security**: Why secrets > random for passwords
- **Algorithm design**: Creating scoring systems and pattern detection
- **Error handling**: Graceful failure with helpful messages
- **Testing strategy**: How to verify your program works correctly

---

## Important Reminders

**Security:**
- Always use `secrets` module, NEVER `random` for password generation
- This is not optional - cryptographic randomness is critical for security

**Code Organization:**
- Keep I/O separate from logic (passgen.py does I/O, other modules don't)
- Each function should do one thing well
- Use meaningful variable names

**Testing:**
- Test each function individually before integration
- Use the `if __name__ == '__main__':` pattern for module-level testing
- Test both valid and invalid inputs

**Learning Process:**
- Implement one function at a time
- Test immediately after writing each function
- Don't move on until current function works
- Google syntax questions - that's appropriate
- Ask for help when genuinely stuck after trying

---

## Resources

**Python Documentation:**
- `string` module: https://docs.python.org/3/library/string.html
- `secrets` module: https://docs.python.org/3/library/secrets.html
- `argparse` tutorial: https://docs.python.org/3/howto/argparse.html
- Type hints: https://docs.python.org/3/library/typing.html

**When to use these:**
- Look up exact syntax for things you conceptually understand
- Explore what's available in a module
- Learn new library features

**When NOT to use these:**
- As a substitute for thinking through the logic
- To find complete implementations to copy

---

## Stretch Goals (Optional)

If you finish and want more challenges:

1. Add passphrase generation (random words instead of random characters)
2. Calculate and display password entropy
3. Check against common password lists
4. Add clipboard support (auto-copy generated passwords)
5. Color-coded terminal output (red=weak, green=strong)
6. Configuration file for saving user preferences
7. Exclude ambiguous characters option (0/O, 1/l/I)

---

## Final Notes

**This spec gives you:**
- Module structure (3 files, clear responsibilities)
- Function signatures (names, parameters, return types)
- High-level requirements (what each function should do)
- Testing guidance (how to verify it works)

**This spec does NOT give you:**
- Implementation details (how to write the logic)
- Exact algorithms (you design the scoring system)
- Step-by-step instructions (you figure out the order)

**The gap between "what" and "how" is where your learning happens.**

You'll struggle. You'll Google things. You'll rewrite functions. You'll debug errors. **This is the process.** This is how you develop real problem-solving skills.

When you finish this project, you'll have:
- A working, professional-quality CLI tool
- Experience with multi-module architecture
- Practice making design decisions
- Confidence in your ability to build from requirements

**Now go build it.**

---

**Estimated Time:** 4-6 hours (or more if you're learning deeply - that's fine)  
**When to ask for help:** After you've attempted something and gotten stuck, not before  
**How to ask for help:** Show what you tried, what happened, what you don't understand

Good luck. You've got this.
