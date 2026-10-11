import re

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


def extract_emails(input_file: str) -> list[str]:
    
    valid_list = []
    with open(input_file, "r", encoding="utf-8") as emails_file:
        for email in emails_file:
            match = EMAIL_PATTERN.search(email)
            if match :
                valid_list.append(match.group() + "\n")

    return valid_list


def save_valid_emails(input_file: str, output_file: str) -> None:
    """
    Validate emails from a text file and save the valid ones to another text file.

    Args:
    
        input_file: Path to the input file.
        output_file: Path to the output file.

    Example:

        import email_utils

        email_utils.save_valid_emails("emails.txt", "valid_emails.txt")


    """
    with open(output_file, "a", encoding="utf-8") as valids_email_file:
        for valid in extract_emails(input_file):
            valids_email_file.write(valid)
            



