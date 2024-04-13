import argparse
import os
from datetime import datetime


def parse_args() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", nargs="+", default=".")
    parser.add_argument("-f", "--file_name", default="file.txt")
    args = parser.parse_args()
    path_to_dir = os.path.join(*args.dir or ["."])
    return path_to_dir, os.path.join(path_to_dir, args.file_name)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{count} {user_input}\n")
            count += 1


def main() -> None:
    path_to_dir, file_path = parse_args()
    os.makedirs(path_to_dir, exist_ok=True)
    create_file(file_path)


if __name__ == "__main__":
    main()
