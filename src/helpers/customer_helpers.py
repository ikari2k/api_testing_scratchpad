from typing import Dict

from src.utils.generic import generate_random_email_and_password


class CustomerHelper:
    def __init__(self) -> None:
        pass

    def create_customer(
        self, email: str | None = None, password: str | None = None, **kwargs
    ) -> dict:
        if not email or email == "":
            email = generate_random_email_and_password()[0]

        if not password or email == "":
            password = "Password1"

        payload = {}
        payload["email"] = email
        payload["password"] = password
        payload.update(kwargs)

        return payload
