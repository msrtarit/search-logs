
import os
import argparse

def search_string_in_files(directory, search_term, context_lines=3):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):  # Only process .txt files
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    
                    for i, line in enumerate(lines):
                        if search_term in line:  
                            start = max(i - context_lines, 0)
                            end = min(i + context_lines + 1, len(lines))
                            print(f"--- Match found in {file_path} ---")
                            for context_line in lines[start:end]:
                                print(context_line.strip())
                            print("-" * 50)
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a string in .txt files and show context.")
    parser.add_argument("search_term", type=str, help="The string to search for.")
    parser.add_argument(
        "--directory",
        type=str,
        default="./log",
        help="The directory containing .txt files (default: ./log)."
    )
    parser.add_argument(
        "--context-lines",
        type=int,
        default=0,
        help="Number of lines to show before and after the match (default: 3)."
    )

    args = parser.parse_args()

    search_string_in_files(args.directory, args.search_term, args.context_lines)
