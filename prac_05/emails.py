"""Emails collector
Estimate: 25 minutes
Actual:   27 minutes
"""

def main():
    email_to_name: dict[str, str] = {}
    while True:
        email = input("Email: ").strip()
        if email == "":
            break
        default_name = extract_name_from_email(email)
        confirm = input(f"Is your name {default_name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            default_name = input("Name: ").strip()
        email_to_name[email] = default_name
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name_from_email(email: str) -> str:
    local = email.split("@", maxsplit=1)[0]
    parts = local.replace(".", " ").replace("_", " ").split()
    return " ".join(parts).title() if parts else "Unknown"

if __name__ == "__main__":
    main()