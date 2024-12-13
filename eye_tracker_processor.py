import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load simulated data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None

# Visualize gaze points as a scatter plot
def plot_gaze_points(data):
    if data is not None:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='x_coordinate', y='y_coordinate', data=data, hue='timestamp', palette='cool')
        plt.title("Gaze Points")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.show()
    else:
        print("No data to plot.")

# Main function
if __name__ == "__main__":
    # Load data from the CSV file
    data = load_data("simulated_eye_data.csv")

    # Plot gaze points
    plot_gaze_points(data)
    # Plot gaze heatmap
    plot_gaze_heatmap(data)
# Visualize gaze points as a heatmap
def plot_gaze_heatmap(data):
    if data is not None:
        plt.figure(figsize=(10, 6))
        sns.kdeplot(
            x=data['x_coordinate'],
            y=data['y_coordinate'],
            cmap="Reds",
            fill=True,
            bw_adjust=0.5
        )
        plt.title("Gaze Heatmap")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.show()
    else:
        print("No data to plot.")
