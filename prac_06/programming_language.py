"""CP1404/CP5632 Practical - Programming Language

Estimate: 10   Start time: 9:42
Actual:   9   End time:   9:51
"""

class ProgrammingLanguage:

    def __init__(self, name: str, typing: str, reflection: bool, year: int):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        return self.typing.lower() == "dynamic"

    def __str__(self) -> str:
        typing_str = f"{self.typing} Typing"
        return f"{self.name}, {typing_str}, Reflection={self.reflection}, First appeared in {self.year}"