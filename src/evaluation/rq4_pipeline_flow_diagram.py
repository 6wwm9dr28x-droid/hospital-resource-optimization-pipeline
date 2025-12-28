import matplotlib.pyplot as plt

OUTPUT_PATH = "figures/RQ4_Fig1.pdf"

def main():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("off")

    steps = [
        "Raw Data\n(Kaggle + HDHI)",
        "Data Ingestion",
        "Data Cleaning",
        "Feature Engineering",
        "Analytics\n(Tables & Figures)"
    ]

    x_positions = range(len(steps))

    for x, step in zip(x_positions, steps):
        ax.text(
            x, 0.5, step,
            ha="center", va="center",
            bbox=dict(boxstyle="round", fc="lightblue")
        )

    for i in range(len(steps) - 1):
        ax.annotate(
            "",
            xy=(i + 1, 0.5),
            xytext=(i + 0.1, 0.5),
            arrowprops=dict(arrowstyle="->")
        )

    ax.set_xlim(-0.5, len(steps) - 0.5)

    plt.title("Hospital Resource Optimization Pipeline Flow")
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ4 FIGURE 1 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()

