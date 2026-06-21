# Production Data Automation

This project automates daily data processing so product managers spend less time on manual reporting and more time on decisions.

## Tech Stack

- Python
- Pandas

## What the script does

The automation script:

- scans the `data_raw/` folder for input files
- loads CSV and JSON data
- normalizes timestamps across records
- aggregates key metrics
- validates data quality against thresholds
- writes a summary output to `data_output/daily_digest.csv`

## Validation logic

The script checks for data quality issues such as:

- error rate threshold
- null rate threshold
- unexpected values or missing fields

If problems are found, it prints alerts so issues can be fixed quickly.

## How to run

1. Clone the repo
2. Create a Python virtual environment
3. Install requirements
4. Place raw files in `data_raw/`
5. Run:

```bash
python -m src.main
```

## Notes

Keep the project simple and narrative-focused, with clear automation of raw input data to a daily digest output.
