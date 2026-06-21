from pathlib import Path
import pandas as pd
from .config import RAW_DATA_DIR

def load_events_files() -> pd.DataFrame:
    frames = []
    for path in RAW_DATA_DIR.glob("events_*.csv"):
        df = pd.read_csv(path)
        df["source_file"] = path.name
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

def load_latency_files() -> pd.DataFrame:
    frames = []
    for path in RAW_DATA_DIR.glob("latency_*.json"):
        df = pd.read_json(path, lines=True)
        df["source_file"] = path.name
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

def load_feedback_files() -> pd.DataFrame:
    frames = []
    for path in RAW_DATA_DIR.glob("feedback_*.csv"):
        df = pd.read_csv(path)
        df["source_file"] = path.name
        frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def to_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def prepare_events(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = to_datetime(df, "timestamp")
    return df

def prepare_latency(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = to_datetime(df, "timestamp")
    df["latency_ms"] = pd.to_numeric(df["latency_ms"], errors="coerce")
    return df

def prepare_feedback(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    df = to_datetime(df, "timestamp")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df

def build_daily_digest(events: pd.DataFrame,
                       latency: pd.DataFrame,
                       feedback: pd.DataFrame) -> pd.DataFrame:
    # Example metrics
    events_count = events.groupby(events["timestamp"].dt.date)["event_type"].count().rename("total_events")
    error_rate = (
        latency.assign(is_error=lambda d: d["status"] >= 500)
               .groupby(latency["timestamp"].dt.date)["is_error"]
               .mean()
               .rename("error_rate")
    )
    avg_latency = latency.groupby(latency["timestamp"].dt.date)["latency_ms"].mean().rename("avg_latency_ms")
    avg_rating = feedback.groupby(feedback["timestamp"].dt.date)["rating"].mean().rename("avg_rating")

    digest = (
        pd.concat([events_count, error_rate, avg_latency, avg_rating], axis=1)
          .reset_index()
          .rename(columns={"index": "date"})
    )
    return digest
