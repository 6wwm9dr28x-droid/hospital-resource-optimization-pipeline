import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "figures/RQ2_Fig2.pdf"

def main():
    df = pd.read_csv(INPUT_PATH)

    plt.figure(figsize=(8, 5))
    sns.histplot(df["length_of_stay"].dropna(), bins=30, kde=True)

    plt.title("Length of Stay Distribution (HDHI Admissions)")
    plt.xlabel("Length of Stay (days)")
    plt.ylabel("Number of Admissions")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ2 FIGURE 2 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
