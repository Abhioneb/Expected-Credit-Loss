import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def compute_ecl(df: pd.DataFrame, segment: str) -> pd.Series:
    sub = df[df["segment_tag"] == segment].copy()
    sub["month"] = sub["date"].dt.to_period("M")
    agg = sub.groupby("month").agg(
        total_amt=("amount", "sum"),
        loss_amt=("default_flag", lambda flags: (flags * sub.loc[flags.index, "amount"]).sum())
    )
    loss_rate = (agg["loss_amt"] / agg["total_amt"]).fillna(0)
    return loss_rate.rolling(3, min_periods=1).mean()

def recommend_action(ecl: pd.Series) -> str:
    latest = ecl.iloc[-1]
    cumulative = ecl.sum()
    if latest > 0.05:
        return "🔺 Increase interest"
    if cumulative > 0.03:
        return "⚠️ Reduce disbursement"
    return "✅ Maintain current terms"