import matplotlib.pyplot as plt

OUTPUT_PATH = "figures/RQ4_Fig2.pdf"

def main():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis("off")

    tasks = {
        "Ingest Appointments": (0, 1),
        "Ingest Admissions": (0, 0),
        "Clean Appointments": (2, 1),
        "Clean Admissions": (2, 0),
        "Feature Engineering": (4, 0),
        "Analytics & Reporting": (6, 0.5)
    }

    # Draw task boxes
    for task, (x, y) in tasks.items():
        ax.text(
            x, y, task,
            ha="center", va="center",
            bbox=dict(boxstyle="round", fc="lightgreen")
        )

    # Draw dependencies (arrows)
    dependencies = [
        ((0, 1), (2, 1)),
        ((0, 0), (2, 0)),
        ((2, 0), (4, 0)),
        ((2, 1), (6, 0.5)),
        ((4, 0), (6, 0.5))
    ]

    for start, end in dependencies:
        ax.annotate(
            "",
            xy=end,
            xytext=start,
            arrowprops=dict(arrowstyle="->")
        )

    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 2)

    plt.title("Pipeline Orchestration DAG (Conceptual)")
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.close()

    print("=== RQ4 FIGURE 2 CREATED ===")
    print("Saved to:", OUTPUT_PATH)

if __name__ == "__main__":
    main()
