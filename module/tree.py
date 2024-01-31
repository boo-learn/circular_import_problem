import random
from .apple import Apple


class AppleTree:
    def __init__(self, num_apples: int = 10):
        self.apples = [Apple(random.choice(("red", "green", "yellow")), self) for _ in range(num_apples)]

    def get_apple(self, index) -> Apple:
        return self.apples[index]

    def add_apple(self, new_apple: Apple) -> None:
        self.apples.append(new_apple)
        new_apple.tree = self

    def __str__(self):
        return f"Tree with {len(self.apples)} apples"
