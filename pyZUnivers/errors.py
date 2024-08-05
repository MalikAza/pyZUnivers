class UserNotFound(Exception):
    def __init__(self, username: str) -> None:
        self.username = username

    def __str__(self) -> str:
        return f'User ({self.username}) does not have a ZUnivers account.'