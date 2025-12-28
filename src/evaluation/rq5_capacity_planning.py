import pandas as pd

INPUT_PATH = "tables/RQ5_Table1.xlsx"
OUTPUT_PATH = "tables/RQ5_Table2.xlsx"

AVERAGE_LOS = 6  # days (from RQ3 median LOS)

def main():
    df = pd.read_excel(INPUT_PATH)

    # Use rolling average as expected admissions
    df["expected_admissions"] = df["rolling_avg"]

    # Estimate beds required
    df["estimated_beds_required"] = df["expected_admissions"] * AVERAGE_LOS

    result = df[["doa", "expected_admissions", "estimated_beds_required"]].tail(14)

    result.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ5 TABLE 2 CREATED ===")
    print(result)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
