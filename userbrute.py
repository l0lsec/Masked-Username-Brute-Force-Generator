import itertools
import string
from tqdm import tqdm

def generate_usernames(template):
    if len(template) < 2:
        raise ValueError("Template must have at least two characters")

    first_char = template[0]
    last_char = template[-1]
    masked_length = len(template) - 2

    chars = string.ascii_lowercase + string.digits
    total_combinations = len(chars) ** masked_length

    for combination in itertools.product(chars, repeat=masked_length):
        yield first_char + ''.join(combination) + last_char

def save_to_file(filename, usernames, total_combinations):
    with open(filename, "w", buffering=100000) as file:
        with tqdm(total=total_combinations, unit="username", desc="Generating usernames") as pbar:
            for username in usernames:
                pbar.update(1)
                file.write(username + "\n")

def main():
    template = input("Enter the masked username (e.g., c******l): ")
    usernames = generate_usernames(template)

    chars = string.ascii_lowercase + string.digits
    total_combinations = len(chars) ** (len(template) - 2)

    filename = "usernames.txt"
    save_to_file(filename, usernames, total_combinations)

    print(f"Usernames have been generated and saved to {filename}")

if __name__ == "__main__":
    main()
