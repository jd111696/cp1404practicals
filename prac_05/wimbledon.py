"""Wimbledon stats
Estimate: 35 minutes
Actual:   ____ minutes
"""

import csv
from collections import Counter

def main():
    filename = "wimbledon.csv"
    records = load_rows(filename)  # list[dict]
    champion_counts = count_champions(records)
    countries = collect_countries(records)

    print("Wimbledon Champions:")
    for champion in sorted(champion_counts):
        print(f"{champion} {champion_counts[champion]}")

    print()
    country_list = sorted(countries)
    print(f"These {len(country_list)} countries have won Wimbledon:")
    print(", ".join(country_list))

def load_rows(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def count_champions(rows: list[dict]) -> dict[str, int]:
    """Rows must contain a 'Champion' column."""
    counter = Counter()
    for row in rows:
        champion = row.get("Champion", "").strip()
        if champion:
            counter[champion] += 1
    return dict(counter)

def collect_countries(rows: list[dict]) -> set[str]:
    """Rows must contain a 'Country' column; prints ISO-like codes or country strings from the CSV."""
    countries: set[str] = set()
    for row in rows:
        country = row.get("Country", "").strip()
        if country:
            countries.add(country)
    return countries

if __name__ == "__main__":
    main(