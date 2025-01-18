import os
from dotenv import load_dotenv
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

CONFIG = {
    "log_file" : os.path.join(PROJECT_ROOT, "logs/process.log"),
    "log_level": "INFO",
    "src_directory": os.path.join(PROJECT_ROOT, "src"),
}