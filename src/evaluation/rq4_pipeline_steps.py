import pandas as pd

OUTPUT_PATH = "tables/RQ4_Table1.xlsx"

def main():
    data = [
        ["Data Ingestion", "Load raw appointment data", "hospital-KaggleV2-May-2016.xlsx"],
        ["Data Ingestion", "Load raw admissions data", "HDHI Admission data111.csv"],
        ["Data Cleaning", "Clean and standardize appointment data", "hospital-KaggleV2-May-2016_cleaned.csv"],
        ["Data Cleaning", "Clean admissions data and compute LOS", "HDHI_Admission_cleaned.csv"],
        ["Feature Engineering", "Create length_of_stay feature", "HDHI_Admission_cleaned.csv"],
        ["Evaluation", "Generate descriptive statistics (RQ1–RQ3)", "Tables & Figures"],
        ["Orchestration", "Execute pipeline stages sequentially", "Reproducible pipeline"]
    ]

    df = pd.DataFrame(
        data,
        columns=["Pipeline Stage", "Description", "Output"]
    )

    df.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ4 TABLE 1 CREATED ===")
    print(df)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
