# Search Logs Script

## Overview

This Python script searches for a given string within multiple `.txt` files inside a specified directory and displays the matching line along with a configurable number of surrounding lines for context.

## Features

- Searches for a specific string in all `.txt` files within a directory.
- Displays the matching line along with a configurable number of surrounding lines.
- Supports command-line arguments for flexibility.
- Handles file reading errors gracefully.

## Prerequisites

- Python 3.x installed

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/msrtarit/search-logs.git
   cd search-logs
   ```
2. (Optional) Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install required dependencies (if any in future versions):
   ```bash
   pip install -r requirements.txt  # No dependencies currently
   ```

## Usage

Run the script with the search term as an argument:

```bash
python search_logs.py <search_term>
```

### Additional Options

- **Specify a different directory** (default: `./log`):
  ```bash
  python search_logs.py <search_term> --directory /path/to/logs
  ```
- **Specify the number of surrounding lines to display** (default: 3):
  ```bash
  python search_logs.py <search_term> --context-lines 5
  ```

### Example

If you want to search for the word `error` in log files inside `/var/logs` and display 5 lines before and after the match:

```bash
python search_logs.py error --directory /var/logs --context-lines 5
```

## Example Output

```
--- Match found in ./log/file1.txt ---
Line before match 1
Line before match 2
This is the line containing error
Line after match 1
Line after match 2
--------------------------------------------------
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing

Feel free to submit issues and pull requests!

## Author

Shahriar Tarit



