import os
from pathlib import Path
import logging

# Create the logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Set up the logging configuration
log_file = "logs/loggin_info.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "service-bdd/Dockerfile",  # Dockerfile for service-bdd
    "service-web-app/Dockerfile",  # Dockerfile for service-web-app
    "service-web-app/app.py",  # Python file for the Flask web app
    "service-web-app/template/index.html",  # HTML template file
    "service-web-app/static/css/style.css",  # CSS file
    "service-web-app/static/js/script.js",  # JavaScript file
    "service-web-app/utils/data_handler.py"  # Data Handling File
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Log the completion of the file creation process
logging.info("File creation process completed")
