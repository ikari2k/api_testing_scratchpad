import logging as logger
import random
import string
from typing import Tuple


def generate_random_email_and_password(
    domain: str = "", email_prefix: str = ""
) -> Tuple[str, str]:
    logger.debug("Generating random email and password")

    if not domain and domain == "":
        domain = "test.com"
    if not email_prefix and domain == "":
        email_prefix = "testuser"

    random_email_string_length = 10
    random_string = "".join(
        random.choices(string.ascii_lowercase, k=random_email_string_length)
    )

    email_string = email_prefix + "_" + random_string + "@" + domain

    password_length = 20
    password_string = "".join(random.choices(string.ascii_letters, k=password_length))

    random_info = {"email": email_string, "password": password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return email_string, password_string
