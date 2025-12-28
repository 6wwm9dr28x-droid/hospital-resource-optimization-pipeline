import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "tables/RQ5_Table1.xlsx"
OUTPUT_PATH = "figures/RQ5_Fig2.pdf"

def main():
    df = pd.read_excel(INPUT_PATH)

    plt.figure(figsize=(10, 5))
    plt.plot(df["doa"], df["rolling_avg"], color="orange")

    plt.title("Forecasted Admission Trend (Rolling Average)")
    plt.xlabel("Date")
    plt.ylabel("Admissions (Rolling Avg)")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ5 FIGURE 2 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
