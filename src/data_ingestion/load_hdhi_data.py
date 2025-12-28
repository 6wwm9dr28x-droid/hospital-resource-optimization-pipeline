import pandas as pd

DATA_PATH = "data/HDHI Admission data111.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    print("=== HDHI DATASET LOADED SUCCESSFULLY ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values per column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    main()
