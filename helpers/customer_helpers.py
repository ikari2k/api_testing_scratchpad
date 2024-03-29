from utils.generic_utils import generate_random_email_and_password


class CustomerHelper:
    def __init__(self) -> None:
        pass

    def create_customer_payload(
        self, email: str | None = None, password: str | None = None, **kwargs
    ) -> dict:
        if not email or email == "":
            email = generate_random_email_and_password()[0]

        if not password or email == "":
            password = "Password1"

        payload = {"email": email, "password": password}
        payload.update(kwargs)

        return payload


if __name__ == "__main__":
    cs = CustomerHelper()
    print(cs.create_customer_payload())
