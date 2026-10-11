# Email Validator

A simple Python tool that extracts email addresses matching a regular expression from a text file and saves them to an output file.

## Features

* Extract email addresses from a text file using regular expressions.
* Match email addresses against a predefined pattern.
* Save extracted email addresses to an output file.
* Separate the main program from reusable utility functions.
* Use type hints and function documentation for readability.

## Technologies

* **Python 3.9+**
* **Regular Expressions (`re`)**
* **File Handling**
* **Functions and Modules**
* **Type Hints**

## Project Structure

```text
email-validator/
│
├── main.py
├── utils/
│   ├── __init__.py
│   └── email_utils.py
│
├── emails.txt
├── valid.txt
├── .gitignore
└── README.md
```

## Usage

### 1. Prepare the input file

Add email addresses or other text containing email addresses to `emails.txt`.

Example:

```text
john@gmail.com
invalid-email
admin@example.org
contact@example.net
```

### 2. Run the program

```bash
python main.py
```

### 3. Check the output

Email addresses matching the regular expression are appended to `valid.txt`.

Example output:

```text
john@gmail.com
admin@example.org
contact@example.net
```

## How It Works

The project is organized into two main Python files:

* **`main.py`** — The entry point that calls the email-processing function.
* **`utils/email_utils.py`** — Contains the regular expression and the functions responsible for extracting and saving matching email addresses.

The `extract_emails()` function reads the input file line by line, searches each line for a match, and collects the matched addresses.

The `save_valid_emails()` function writes the extracted addresses to the output file.

## Concepts Practiced

Through this project, I practiced:

* Writing and compiling regular expressions.
* Reading and writing text files.
* Working with Python functions and modules.
* Using type annotations.
* Organizing code into reusable components.
* Processing text and extracting matching patterns.

## Limitations

* Regular expressions check whether an address matches a pattern; they do not confirm that the address exists or can receive email.
* The current implementation extracts at most one matching email address per input line.
* Results are appended to `valid.txt`, so repeated runs can produce duplicate entries.

## Future Improvements

* Remove duplicate email addresses.
* Support multiple email addresses on the same line.
* Add command-line arguments for input and output file paths.
* Handle missing input files and file access errors.
* Add an option to overwrite the output file instead of appending.
* Improve validation and add automated tests.

## License

This project is intended for educational purposes. Add a `LICENSE` file if you want to distribute it under a specific open-source license.
