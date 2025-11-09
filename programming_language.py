"""CP1404 Practical - ProgrammingLanguage

Estimate: 15 minutes   Start time: 1958
Actual:   17 minutes   End time: 2015
"""


class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, year and pointer arithmetic support."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialise a ProgrammingLanguage instance.

        reflection and pointer_arithmetic are expected to be Boolean values.
        """
        self.name = name
        self.typing = typing            # "Static" or "Dynamic"
        self.reflection = reflection    # True / False
        self.year = year                # int
        self.pointer_arithmetic = pointer_arithmetic  # True / False

    def is_dynamic(self):
        """Return True if language uses dynamic typing."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a nicely formatted string for this language."""
        typing_str = f"{self.typing} Typing"
        return (f"{self.name}, {typing_str}, Reflection={self.reflection}, "
                f"Pointer Arithmetic={self.pointer_arithmetic}, First appeared in {self.year}")