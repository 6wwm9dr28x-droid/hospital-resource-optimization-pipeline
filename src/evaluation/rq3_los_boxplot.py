import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "figures/RQ3_Fig2.pdf"

def main():
    df = pd.read_csv(INPUT_PATH)

    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df["length_of_stay"].dropna())

    plt.title("Length of Stay Distribution (Boxplot)")
    plt.ylabel("Length of Stay (days)")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ3 FIGURE 2 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
