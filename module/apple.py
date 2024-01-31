from typing import Literal
from .tree import AppleTree


class Fruit:
    pass


class Apple(Fruit):
    def __init__(self, color: Literal["red", "green", "yellow"], parent_tree: 'AppleTree' | None = None):
        self.tree = parent_tree
        self.color = color

    def __str__(self):
        return f"{self.color} Apple on {self.tree}"
