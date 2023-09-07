# Вопрос: Если в send_email вместо pass написать return None, то mypy жалуется
#   следующим образом:
#  error: "send_email" does not return a value  [func-returns-value]
# Почему так и как ему сказать, что так и должно быть?

from constants import ___


def send_email(header: str, text_content: str, send_to: str) -> None:
    pass


if __name__ == "__main__":
    assert send_email(header="Test email", text_content="This is a test email", send_to="test@gmail.com") is None
