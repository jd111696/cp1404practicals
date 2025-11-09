"""CP1404/CP5632 Practical - Language file reader using ProgrammingLanguage.

Estimate: ? minutes   Start time: ?
Actual:   ? minutes   End time: ?
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read languages from CSV file, build objects, and display them."""
    filename = "languages.csv"
    languages = load_languages(filename)
    print(f"Languages loaded from {filename}:")
    for language in languages:
        print(language)

    print("\nDynamically typed languages:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


def load_languages(filename):
    """Load ProgrammingLanguage objects from a CSV file."""
    languages = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            if len(parts) != 5:
                continue
            name = parts[0]
            typing = parts[1]
            reflection_text = parts[2]
            year_text = parts[3]
            pointer_text = parts[4]

            reflection = reflection_text.strip().lower() == "yes"
            pointer_arithmetic = pointer_text.strip().lower() == "yes"
            year = int(year_text)

            language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
            languages.append(language)
    return languages


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open("languages.csv", "r", newline="", encoding="utf-8")
    in_file.readline()
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open("languages.csv", "r", newline="", encoding="utf-8")
    file_field_names = in_file.readline().strip().split(",")
    print(file_field_names)
    Language = namedtuple("Language", "name typing reflection year pointer_arithmetic")
    reader = csv.reader(in_file)

    for row in reader:
        if len(row) != 5:
            continue
        language = Language._make(row)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple("Language", "name typing reflection year pointer_arithmetic")
    in_file = open("languages.csv", "r", encoding="utf-8")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, "was released in", language.year)
        print(repr(language))
    in_file.close()


if __name__ == "__main__":
    main()