import pandas as pd

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "tables/RQ3_Table1.xlsx"

def main():
    df = pd.read_csv(INPUT_PATH, parse_dates=["doa"])

    # Aggregate admissions per day
    daily_admissions = (
        df.groupby(df["doa"].dt.date)
        .size()
        .reset_index(name="daily_admissions")
    )

    daily_admissions.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ3 TABLE 1 CREATED ===")
    print(daily_admissions.head())
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()

