import subprocess
import datetime
import os

# Create a directory for reports if it doesn't exist
report_dir = os.path.join(os.getcwd(), "reports")
os.makedirs(report_dir, exist_ok=True)

# Generate a timestamp for the report filename
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# Report file path and name
report_file = os.path.join(report_dir, f"report_{timestamp}.html")

# Command to run pytest with HTML report generation
command = [
    "pytest",
    f"--html={report_file}",
    "--self-contained-html"
]

# Execute the command
subprocess.run(command)