import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_PATH = "data/hospital-KaggleV2-May-2016_cleaned.csv"
OUTPUT_PATH = "figures/RQ1_Fig1.pdf"

def main():
    df = pd.read_csv(INPUT_PATH)

    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], bins=30, kde=True)

    plt.title("Age Distribution of Hospital Appointments")
    plt.xlabel("Age")
    plt.ylabel("Number of Appointments")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ1 FIGURE CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
