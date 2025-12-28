import pandas as pd

OUTPUT_PATH = "tables/RQ4_Table2.xlsx"

def main():
    data = [
        ["Raw Data", "hospital-KaggleV2-May-2016.xlsx", "Excel to CSV conversion", "hospital-KaggleV2-May-2016.csv"],
        ["Raw Data", "HDHI Admission data111.csv", "CSV loading", "HDHI raw dataframe"],
        ["Cleaned Data", "hospital-KaggleV2-May-2016.csv", "Cleaning & normalization", "hospital-KaggleV2-May-2016_cleaned.csv"],
        ["Cleaned Data", "HDHI raw dataframe", "Cleaning & LOS calculation", "HDHI_Admission_cleaned.csv"],
        ["Analytics", "Cleaned datasets", "Aggregation & visualization", "Tables & Figures"]
    ]

    df = pd.DataFrame(
        data,
        columns=["Stage", "Input", "Process", "Output"]
    )

    df.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ4 TABLE 2 CREATED ===")
    print(df)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()

