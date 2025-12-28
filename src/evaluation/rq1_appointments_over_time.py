import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = "data/hospital-KaggleV2-May-2016_cleaned.csv"
OUTPUT_PATH = "figures/RQ1_Fig2.pdf"

def main():
    df = pd.read_csv(
        INPUT_PATH,
        parse_dates=["appointmentday"]
    )

    # Aggregate appointments per day
    daily_counts = (
        df.groupby(df["appointmentday"].dt.date)
        .size()
        .reset_index(name="appointments")
    )

    plt.figure(figsize=(10, 5))
    plt.plot(daily_counts["appointmentday"], daily_counts["appointments"])

    plt.title("Daily Hospital Appointment Volume Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Appointments")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ1 FIGURE 2 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
