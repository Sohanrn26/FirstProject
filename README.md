# Log Analyzer

A simple Python-based log analysis tool that reads application log files and helps identify important log entries such as errors, warnings, and other relevant information.

## Features

- Reads and analyzes log files
- Identifies error and warning messages
- Searches logs for specific patterns
- Provides a simple summary of matching log entries
- Can be extended with additional log-analysis functionality

## Project Structure

```text
tiny_python_project/
│
├── logAnalyser.py
└── README.md
```

## Requirements

- Python 3.x
- Git

No external Python packages are required for the basic version.

## How to Run

Clone the repository:

```bash
git clone https://github.com/Sohanrn26/FirstProject.git
```

Move into the project directory:

```bash
cd FirstProject
```

Run the analyzer:

```bash
python logAnalyser.py
```

## Example

The analyzer can be used to process application logs and identify important entries such as:

```text
ERROR
WARNING
INFO
```

This can help during troubleshooting by making it easier to locate relevant information in large log files.

## Git Workflow Used

This project is also being used to practice a real-world Git workflow:

```text
Create / modify files
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
git push
        ↓
GitHub
```

## Future Improvements

- Add automated tests using `pytest`
- Add command-line arguments
- Support multiple log-file formats
- Generate log statistics
- Add date/time filtering
- Add CI/CD using Jenkins or GitHub Actions
- Containerize the application using Docker

## Author

Sohan