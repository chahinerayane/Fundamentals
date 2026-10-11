from utils.email_utils import save_valid_emails


email_pattern = r"([A-Za-z0-9\.]+@[A-Za-z0-9]+\.)(com|net|org|info)"



save_valid_emails("emails.txt", "valid.txt")