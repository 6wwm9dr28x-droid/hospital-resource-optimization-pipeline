import pandas as pd

INPUT_PATH = "data/hospital-KaggleV2-May-2016.csv"
OUTPUT_PATH = "data/hospital-KaggleV2-May-2016_cleaned.csv"

def main():
    df = pd.read_csv(INPUT_PATH)

    # Standardize column names (best practice)
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace("-", "_")
    )

    # Convert date columns to datetime
    df["scheduledday"] = pd.to_datetime(df["scheduledday"])
    df["appointmentday"] = pd.to_datetime(df["appointmentday"])

    # Convert categorical fields
    df["gender"] = df["gender"].astype("category")
    df["no_show"] = df["no_show"].astype("category")

    # Sanity checks
    print("=== CLEANING COMPLETED ===")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("\nData types:")
    print(df.dtypes)

    # Save cleaned dataset
    df.to_csv(OUTPUT_PATH, index=False)
    print("\nSaved cleaned data to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
