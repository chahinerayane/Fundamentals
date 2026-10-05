# 🔐 Python Password Generator

A simple command-line password generator built with Python.

This project generates random passwords with a minimum length of 4 characters while ensuring that every generated password contains at least one number, lowercase letter, uppercase letter, and special character.

The generated password is shuffled before being displayed to avoid predictable character placement.

## Features

* Generate passwords with a custom length
* Minimum password length of 4 characters
* At least one number
* At least one lowercase letter
* At least one uppercase letter
* At least one special character
* Randomly shuffle generated characters
* Input validation
* No external dependencies

## Example

```text
Enter the password length: 16

m!9AxQ#7uZ1@Lp5%
```

## How It Works

The generator first creates the required character set:

```text
1 number
1 lowercase letter
1 uppercase letter
1 special character
```

It then fills the remaining characters by randomly selecting from all available character groups.

Finally, the characters are shuffled to prevent the required characters from always appearing in predictable positions.

## Technologies

* Python
* Python Standard Library

The project uses:

* `random`
* `string`

## Requirements

* Python 3.x

No external packages are required.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

Run the program:

```bash
python main.py
```

## What I Practiced

This project helped me practice:

* Python functions
* Loops
* Conditional statements
* Input validation
* String manipulation
* Lists
* List conversion and joining
* Importing from the Python standard library
* Random selection
* Code organization

## Project Structure

```text
password-generator/
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

## Security Note

This project is primarily a **Python learning project**.

The current implementation uses Python's `random` module, which is **not designed for cryptographic security**. It should therefore not be relied upon for generating passwords for high-security or sensitive accounts.

For a security-focused version, Python's `secrets` module should be used instead.

## Future Improvements

* Replace `random` with Python's `secrets` module
* Add command-line arguments with `argparse`
* Add password strength estimation
* Add clipboard support
* Add a GUI using Tkinter
* Add automated tests
* Allow users to choose required character types
* Add an option to exclude ambiguous characters

## Project Status

**Completed — Learning Project**

This project was created as part of my Python learning journey to practice functions, loops, input validation, string manipulation, and Python's standard library.

It may be improved in the future with security-focused randomness and additional functionality.

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more information.
