from datetime import datetime

def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in entries:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(logs)