"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    subject_records = load_subject_records(FILENAME)
    display_subject_details(subject_records)

def load_subject_records(filename=FILENAME):
    input_file = open(filename)
    records = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        records.append(parts)
    input_file.close()
    return records

def display_subject_details(records):
    for code, lecturer, students in records:
        print(f"{code} is taught by {lecturer} and has {students} students")


main()