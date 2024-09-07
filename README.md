# Username Brute Force Generator

## Overview

The **Username Brute Force Generator** is a Python script that generates potential usernames based on a provided masked template, leveraging a brute-force approach. This tool is particularly useful for cybersecurity professionals, ethical hackers, and penetration testers needing to create a list of possible usernames for testing purposes.

This script combines the power of Python’s `itertools` to generate all possible combinations of usernames, with a focus on templates where only certain characters are known (such as the first and last character), while the middle is replaced by combinations of lowercase letters and digits.

## Key Features

- **Generate Custom Usernames**: Provide a template like `j******n`, and the script will brute-force all possible combinations for the masked part.
- **Efficient Combination Handling**: Uses the powerful `itertools` library to efficiently handle the generation of all possible combinations.
- **Progress Display**: The script displays a real-time progress bar using `tqdm`, providing clear feedback on generation progress.
- **Save to File**: Outputs generated usernames to a file (`usernames.txt`) for easy access.

## Use Cases

- **Cybersecurity Penetration Testing**: Generate possible username combinations for brute-force attacks during penetration testing and red teaming engagements.
- **Credential Enumeration**: Useful for generating large lists of usernames for credential stuffing or enumeration tests.
- **Data Preparation**: Prepare large datasets of usernames for testing authentication systems or databases.
  
## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/l0lsec/Masked-Username-Brute-Force-Generator.git
    cd Masked-Username-Brute-Force-Generator
    ```

2. **Install Dependencies:**
    You will need the following Python libraries:
    ```bash
    pip install tqdm
    ```

## Usage

### Running the Script

1. **Execute the script:**
   ```bash
   python userbrute.py
   ```

2. **Input the template** when prompted:
   - Use asterisks (`*`) for unknown characters. Example: `j******n` will generate all possible usernames starting with `j` and ending with `n`.
   
   Example Input:
   ```
   Enter the masked username (e.g., c******l): j*****n
   ```

3. **Output**:
   - The script generates all possible combinations and saves them into `usernames.txt`.
   - Progress is shown via a progress bar.

### Example
Input:
```
j******n
```

Output (saved to `usernames.txt`):
```
j000000n
j000001n
j000002n
...
```

## Customization

You can modify the script to:
- **Change the character set**: Add or remove characters from `string.ascii_lowercase + string.digits` to adjust which characters are included in the generated combinations.
- **Adjust output file format**: Modify the `save_to_file` function to output in other formats (e.g., CSV, JSON).

## Contributing

Feel free to submit issues or pull requests if you'd like to improve the script or add additional features. Contributions to optimize performance or extend functionality (e.g., support for special characters) are welcome!

## License

This project is licensed under the MIT License.

## SEO Keywords

- Username brute force generator
- Penetration testing username lists
- Username wordlist generator
- Python username generator tool
- Credential brute-force username generator
- Username pattern generator Python
- Tqdm progress bar for large files
- Python itertools username combinations
- Generate username list cybersecurity
- Username enumeration tool

## Contact

For any questions or feedback, feel free to reach out. Links in bio.
