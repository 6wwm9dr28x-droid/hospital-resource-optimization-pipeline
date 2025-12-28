import pandas as pd

INPUT_PATH = "data/hospital-KaggleV2-May-2016_cleaned.csv"
OUTPUT_PATH = "tables/RQ1_Table2.xlsx"

def main():
    df = pd.read_csv(INPUT_PATH)

    schema = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Description": [
            "Unique patient identifier",
            "Unique appointment identifier",
            "Patient gender",
            "Date appointment was scheduled",
            "Actual appointment date",
            "Patient age",
            "Patient neighbourhood",
            "Scholarship indicator",
            "Hypertension indicator",
            "Diabetes indicator",
            "Alcoholism indicator",
            "Disability indicator",
            "SMS reminder received",
            "Appointment no-show indicator"
        ]
    })

    schema.to_excel(OUTPUT_PATH, index=False)

    print("=== RQ1 TABLE 2 CREATED ===")
    print(schema)
    print("\nSaved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
