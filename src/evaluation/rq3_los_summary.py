import pandas as pd

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "tables/RQ3_Table2.xlsx"

def main():
    df = pd.read_csv(INPUT_PATH)

    los = df["length_of_stay"].dropna()

    summary = pd.DataFrame({
        "Metric": ["Mean LOS", "Median LOS", "Minimum LOS", "Maximum LOS"],
        "Value": [
            los.mean(),
            los.median(),
            los.min(),
            los.max()
        ]
    })

    summary.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ3 TABLE 2 CREATED ===")
    print(summary)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
