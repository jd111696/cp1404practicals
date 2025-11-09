"""CP1404 Practical - ProgrammingLanguage

Estimate: 10 minutes   Start time: 2016
Actual:   11 minutes   End time: 2027
"""


class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, year and pointer arithmetic support."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a nicely formatted string for this language."""
        typing_str = f"{self.typing} Typing"
        return (f"{self.name}, {typing_str}, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)
    cplusplus = ProgrammingLanguage("C++", "Static", False, 1983, True)
    print(ruby)
    print(python)
    print(visual_basic)
    print(cplusplus)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()