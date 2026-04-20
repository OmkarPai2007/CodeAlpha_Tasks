import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()

        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", content)
        unique_emails = set(emails)

        with open(output_file, "w") as file:
            for email in unique_emails:
                file.write(email + "\n")

        print(f"{len(unique_emails)} emails extracted successfully!")

    except FileNotFoundError:
        print("Input file not found!")

# User input
input_file = input("Enter input file name (e.g., abc.txt): ")
output_file = input("Enter output file name (e.g., xyz.txt): ")

extract_emails(input_file, output_file)
