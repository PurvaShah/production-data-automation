"""Project configuration constants."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data_raw"
OUTPUT_DIR = BASE_DIR / "data_output"

DAILY_OUTPUT_FILE = OUTPUT_DIR / "daily_digest.csv"


EVENTS_FILE = RAW_DATA_DIR / "events_day1.csv"
FEEDBACK_FILE = RAW_DATA_DIR / "feedback_day1.csv"
LATENCY_FILE = RAW_DATA_DIR / "latency_day1.json"


DEFAULTS = {
    "root_dir": BASE_DIR,
    "data_raw_dir": RAW_DATA_DIR,
    "data_output_dir": OUTPUT_DIR,
    "events_file": EVENTS_FILE,
    "feedback_file": FEEDBACK_FILE,
    "latency_file": LATENCY_FILE,
    "output_csv": DAILY_OUTPUT_FILE,
}



# thresholds for validation
MAX_ERROR_RATE = 0.05      # 5%
MAX_NULL_RATE = 0.10       # 10%
