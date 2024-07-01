# Server Health Check Script

This project involves creating a Python script to monitor the health of a server by checking key metrics such as CPU usage, memory usage, and disk usage. Additionally, the script includes a feature to back up log files every 30 days.

## Project Structure
health_check_project/
│
├── health_check.py
├── requirements.txt
├── README.md
└── logs/
└── health_check.log
└── backup/

- **health_check.py**: The main Python script for health checks.
- **requirements.txt**: A file containing the project's dependencies.
- **README.md**: Documentation for the project.
- **logs/**: Directory to store log files and backups.

## Prerequisites

Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/health_check_project.git
cd health_check_project

```
 ### Step 2 : Create andd Activate a Virtual Env
 Create a virtual environment to manage dependencies:

 ```bash 
   python -m venv venv 
   ```

Activate the virtual environment:
- **On Windows:**
```bash
venv\Scripts\activate
```

- **On macOs/Linux:**
```bash
source venv/bin/activate
```

### Step 3 : Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### Usage
Run the script to perform a server health check:
```bash
python health_check.py
```
The script will log CPU usage, memory usage, and disk usage in logs/health_check.log. If the log file is older than 30 days, it will be backed up to the logs/backup/ directory.

## Features 
- **CPU Usage Monitoring:** Logs the CPU usage percentage. If usage exceeds 80%, a warning is logged.
- **Memory Usage Monitoring:** Logs the memory usage percentage. If usage exceeds 80%, a warning is logged.
- **Disk Usage Monitoring:** Logs the disk usage percentage. If usage exceeds 80%, a warning is logged.
- **Log Backup:** Backs up the log file every 30 days to the logs/backup/ directory.
- To regularly back up log files, prevent data loss, and preserve historical records, the Python standard libraries shutil and datetime were used. The os module was utilized to interact with the operating system.