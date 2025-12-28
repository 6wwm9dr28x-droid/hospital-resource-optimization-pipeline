import pandas as pd

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "tables/RQ5_Table1.xlsx"

def main():
    df = pd.read_csv(INPUT_PATH, parse_dates=["doa"])

    daily = (
        df.groupby(df["doa"].dt.date)
        .size()
        .reset_index(name="actual_admissions")
    )

    daily["doa"] = pd.to_datetime(daily["doa"])
    daily = daily.sort_values("doa")

    # Rolling average (7-day)
    daily["rolling_avg"] = daily["actual_admissions"].rolling(window=7).mean()

    # Forecast next 14 days using last rolling average
    last_date = daily["doa"].max()
    last_value = daily["rolling_avg"].iloc[-1]

    forecast_dates = pd.date_range(
        start=last_date + pd.Timedelta(days=1),
        periods=14
    )

    forecast = pd.DataFrame({
        "doa": forecast_dates,
        "actual_admissions": [None] * 14,
        "rolling_avg": [last_value] * 14
    })

    result = pd.concat([daily, forecast], ignore_index=True)

    result.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ5 TABLE 1 CREATED ===")
    print(result.tail())
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
