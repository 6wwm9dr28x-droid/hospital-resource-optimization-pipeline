import pandas as pd

INPUT_PATH = "data/hospital-KaggleV2-May-2016_cleaned.csv"
OUTPUT_PATH = "tables/RQ1_Table1.xlsx"

def main():
    df = pd.read_csv(
        INPUT_PATH,
        parse_dates=["scheduledday", "appointmentday"]
    )

    # Basic KPIs
    total_appointments = len(df)
    no_show_rate = (df["no_show"] == "Yes").mean()
    avg_age = df["age"].mean()
    median_age = df["age"].median()

    summary = pd.DataFrame({
        "Metric": [
            "Total Appointments",
            "No-show Rate",
            "Average Age",
            "Median Age"
        ],
        "Value": [
            total_appointments,
            round(no_show_rate, 3),
            round(avg_age, 2),
            median_age
        ]
    })

    summary.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ1 TABLE CREATED ===")
    print(summary)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
