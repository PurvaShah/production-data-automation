from .etl import (
    load_events_files,
    load_latency_files,
    load_feedback_files,
    prepare_events,
    prepare_latency,
    prepare_feedback,
    build_daily_digest,
)
from .validation import validate_digest
from .config import OUTPUT_DIR, DAILY_OUTPUT_FILE

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    events_raw = load_events_files()
    latency_raw = load_latency_files()
    feedback_raw = load_feedback_files()

    events = prepare_events(events_raw)
    latency = prepare_latency(latency_raw)
    feedback = prepare_feedback(feedback_raw)

    digest = build_daily_digest(events, latency, feedback)

    validate_digest(digest)

    digest.to_csv(DAILY_OUTPUT_FILE, index=False)
    print(f"[INFO] Daily digest written to: {DAILY_OUTPUT_FILE}")

if __name__ == "__main__":
    main()
