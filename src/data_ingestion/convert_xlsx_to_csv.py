import pandas as pd

INPUT_PATH = "data/hospital-KaggleV2-May-2016.xlsx"
OUTPUT_PATH = "data/hospital-KaggleV2-May-2016.csv"

def main():
    # Read the correct sheet
    df_raw = pd.read_excel(INPUT_PATH, sheet_name="in", header=None)

    # The data is stored as a single column -> split by comma
    df = df_raw[0].str.split(",", expand=True)

    # First row is header
    df.columns = df.iloc[0]
    df = df[1:]

    # Reset index
    df.reset_index(drop=True, inplace=True)

    df.to_csv(OUTPUT_PATH, index=False)

    print("Conversion successful (FIXED)")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
