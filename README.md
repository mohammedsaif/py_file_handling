# Python Demo: Student Records & File Handling

A small beginner-friendly Python project that shows how to work with text files. It has two scripts:

- **`sms.py`**: an interactive, menu-driven Student Management System that stores records in a plain text file.
- **`main.py`**: a walkthrough of Python's core file operations (write, read, append, error handling).

No third-party packages are needed, only the Python standard library.

## Requirements

- Python 3.6 or newer (the code uses f-strings)

## Project structure

```
python-demo-1/
├── main.py         # File I/O examples (write, read, append, exceptions)
├── sms.py          # Interactive student management menu
├── students.txt    # Data file where student records are stored
└── README.md
```

## Getting started

```bash
git clone <your-repo-url>
cd python-demo-1
```

### Run the student manager

```bash
python sms.py
```

You'll see a menu:

```
1. Add student
2. View students
3. Exit
Choose an option:
```

| Option | What it does |
| ------ | ------------ |
| `1` | Prompts for a name and course, then appends them to `students.txt` |
| `2` | Prints every saved record (or a friendly message if there are none) |
| `3` | Exits the program |

Example `students.txt` after adding two students:

```
Name: Mohammed
Course: Python
-------------------------
Name: Ahmed
Course: Javascript
-------------------------
```

### Run the file-handling demo

```bash
python main.py
```

> **Note:** `main.py` opens `students.txt` in write mode (`"w"`), which **overwrites any existing records**. Back up the file first if you want to keep your data.

## What `main.py` demonstrates

1. **Writing** a file with `open(..., "w")` and `write()`
2. **Reading** the whole file with `read()`
3. **Reading line by line** with `readline()` inside a `with` block
4. **Appending** to a file with mode `"a"`
5. **Handling errors** with `try / except / finally`:
   - `FileNotFoundError`
   - `PermissionError`
   - `OSError`

## What `sms.py` demonstrates

- Functions to separate responsibilities (`add_student`, `view_students`)
- A `while True` menu loop with input validation
- Using `with open(...)` so files are always closed properly
- Explicit `encoding="utf-8"` for portable text files
- Graceful error handling when the file is missing or can't be read or written

## Ideas for improvement

- Validate input (reject empty names or courses)
- Add search, edit, and delete options
- Store records as JSON or CSV instead of plain text
- Wrap the menu in a `main()` function guarded by `if __name__ == "__main__":`
- Add unit tests

## Author

Mohammed Saif
