import pandas as pd
import matplotlib.pyplot as plt

RAW_PATH = "data/HDHI Admission data111.csv"
CLEAN_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "figures/RQ2_Fig1.pdf"

def main():
    df_raw = pd.read_csv(RAW_PATH)
    df_clean = pd.read_csv(CLEAN_PATH)

    missing_raw = df_raw.isnull().sum()
    missing_clean = df_clean.isnull().sum()

    comparison = pd.DataFrame({
        "Before Cleaning": missing_raw,
        "After Cleaning": missing_clean
    })

    comparison = comparison.loc[comparison.sum(axis=1) > 0]

    comparison.plot(
        kind="bar",
        figsize=(12, 6)
    )

    plt.title("Missing Values Before vs After Cleaning (HDHI Dataset)")
    plt.ylabel("Number of Missing Values")
    plt.xlabel("Column")
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ2 FIGURE 1 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
