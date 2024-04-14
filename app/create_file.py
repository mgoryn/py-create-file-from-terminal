import os
import argparse
from datetime import datetime
from typing import List, Optional


def create_file(
        directory: Optional[str], filename: Optional[str], content: List[str]
) -> None:
    # Create directory if it doesn't exist
    if directory:
        os.makedirs(directory, exist_ok=True)
        return  # Exit function if only creating directories

    # If directory is None but filename is provided, create the file
    if filename:
        filepath = filename
    else:
        print("Please provide either -d or -f flag.")
        return

    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check if file exists, if yes, append content
    if os.path.exists(filepath):
        with open(filepath, 'a') as file:
            file.write('\n\n' + timestamp + '\n')
            for line in content:
                file.write(line + '\n')
    else:
        with open(filepath, 'w') as file:
            file.write(timestamp + '\n')
            for line in content:
                file.write(line + '\n')


def main() -> None:
    parser = argparse.ArgumentParser(description="Create directory or file with content")
    parser.add_argument("-d", "--directory", nargs='+', help="Directory path to create")
    parser.add_argument("-f", "--filename", help="File name to create")
    args = parser.parse_args()

    # Call create_file function with provided arguments
    create_file(args.directory, args.filename, [])
    print("Directory/File created successfully.")


if __name__ == "__main__":
    main()
