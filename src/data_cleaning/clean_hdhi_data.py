import pandas as pd

INPUT_PATH = "data/HDHI Admission data111.csv"
CLEAN_PATH = "data/HDHI_Admission_cleaned.csv"
TABLE_BEFORE = "tables/RQ2_Table1.xlsx"
TABLE_AFTER = "tables/RQ2_Table2.xlsx"

def data_quality_table(df):
    return pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum()
    })

def main():
    # ------------------
    # LOAD RAW DATA
    # ------------------
    df_raw = pd.read_csv(INPUT_PATH)

    quality_before = data_quality_table(df_raw)
    quality_before.to_excel(TABLE_BEFORE, index=False)

    # ------------------
    # CLEAN DATA
    # ------------------
    df = df_raw.copy()

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(".", "", regex=False)
        .str.replace("/", "_")
        .str.replace("-", "_")
    )

    # Parse dates
    df["doa"] = pd.to_datetime(df["doa"], errors="coerce")
    df["dod"] = pd.to_datetime(df["dod"], errors="coerce")

    # Compute Length of Stay (LOS)
    df["length_of_stay"] = (df["dod"] - df["doa"]).dt.days

    # Replace negative or invalid LOS with NaN
    df.loc[df["length_of_stay"] < 0, "length_of_stay"] = pd.NA

    # ------------------
    # SAVE CLEAN DATA
    # ------------------
    df.to_csv(CLEAN_PATH, index=False)

    quality_after = data_quality_table(df)
    quality_after.to_excel(TABLE_AFTER, index=False)

    # ------------------
    # LOG OUTPUT
    # ------------------
    print("=== HDHI CLEANING COMPLETED ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nSaved cleaned data to:", CLEAN_PATH)
    print("\nSaved tables:")
    print(TABLE_BEFORE)
    print(TABLE_AFTER)

if __name__ == "__main__":
    main()
