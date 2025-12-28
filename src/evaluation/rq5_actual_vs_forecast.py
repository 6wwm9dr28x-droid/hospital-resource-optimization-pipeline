import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "tables/RQ5_Table1.xlsx"
OUTPUT_PATH = "figures/RQ5_Fig1.pdf"

def main():
    df = pd.read_excel(INPUT_PATH)

    plt.figure(figsize=(10, 5))

    plt.plot(df["doa"], df["actual_admissions"], label="Actual Admissions")
    plt.plot(df["doa"], df["rolling_avg"], label="Forecast (Rolling Avg)")

    plt.title("Actual vs Forecasted Hospital Admissions")
    plt.xlabel("Date")
    plt.ylabel("Admissions")
    plt.legend()

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ5 FIGURE 1 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
