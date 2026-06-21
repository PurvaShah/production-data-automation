import pandas as pd
from .config import MAX_ERROR_RATE, MAX_NULL_RATE

def compute_null_rate(df: pd.DataFrame) -> float:
    if df.empty:
        return 0.0
    return df.isna().mean().mean()

def validate_digest(digest: pd.DataFrame) -> None:
    if digest.empty:
        print("[WARN] Daily digest is empty. No data processed.")
        return

    # Example: check error rate
    if "error_rate" in digest.columns:
        max_error = digest["error_rate"].max()
        if max_error > MAX_ERROR_RATE:
            print(f"[ALERT] Error rate too high: {max_error:.2%} (threshold {MAX_ERROR_RATE:.2%})")

    # Example: check null rate
    null_rate = compute_null_rate(digest)
    if null_rate > MAX_NULL_RATE:
        print(f"[ALERT] Null rate too high in digest: {null_rate:.2%} (threshold {MAX_NULL_RATE:.2%})")
    else:
        print(f"[INFO] Data quality OK. Null rate: {null_rate:.2%}")
