# main.py


# Constant
from spill import load_spill_data, save_summary, DATA_FILE
import matplotlib.pyplot as plt
import os

# Creating the Graph
def plot_bar_chart(counter, title, xlabel, ylabel, output_path, top_n=10):
    top_items = counter.most_common(top_n)
    if not top_items:
        print(f"[!] No data to plot for {title}")
        return
    labels, values = zip(*top_items)

    plt.figure(figsize=(12, 6))
    plt.bar(labels, values, color='magenta')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    print(f"Saved graph: {output_path}")
    plt.close()


# Saving the Output into the output folder
def main():
    print("Loading data...")
    spills, county_counts, substance_counts = load_spill_data(DATA_FILE)

    # Create the graphs
    plot_bar_chart(county_counts, "Where Are the Spills?", "County Names", "Number of Spills", "output/spills_by_county.png")
    plot_bar_chart(substance_counts, "What Are the Most Common Spills?", "Material Name", "Number of Spills", "output/spills_by_material.png")

    # Saves the summary
    save_summary(county_counts, substance_counts, "output/spill_summary.txt")
    print("Done! The Output saved to /output folder")

if __name__ == '__main__':
    main()