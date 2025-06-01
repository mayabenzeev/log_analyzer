# Log Analyzer CLI Tool

This is a command-line tool that parses log files and generates reports.

## Features

- Parse structured log files
- Generate reports:
  - `summary`: Total entries and count per log level
  - `top-user`: User with the most entries
  - `common-error`: Most frequent error message
- Run locally or via Docker

## Requirements

- Python 3.8+
- Docker (optional)

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python -m analyzer.main --input sample.log --report summary
```

### Using Docker

```
docker build -t log-analyzer .
docker run -v $(pwd):/data log-analyzer --input /data/sample.log --report summary
```

## Running Tests

```
pytest
```

## Example Log Format

```
[2025-06-01 10:03:15] alice:INFO: Login succeeded
[2025-06-01 10:04:12] bob:ERROR: Invalid password
```

