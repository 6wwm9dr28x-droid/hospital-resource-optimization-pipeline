import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "data/HDHI_Admission_cleaned.csv"
OUTPUT_PATH = "figures/RQ3_Fig1.pdf"

def main():
    df = pd.read_csv(INPUT_PATH, parse_dates=["doa"])

    daily = (
        df.groupby(df["doa"].dt.date)
        .size()
        .reset_index(name="admissions")
    )

    plt.figure(figsize=(10, 5))
    plt.plot(daily["doa"], daily["admissions"])

    plt.title("Hospital Admissions Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Admissions")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ3 FIGURE 1 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
