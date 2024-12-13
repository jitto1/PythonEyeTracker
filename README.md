# PythonEyeTracker
# Eye Tracker Data Processor

## Description
The Eye Tracker Data Processor is a Python-based tool designed to visualize and analyze eye-tracking data. It processes gaze data from CSV files and generates visualizations, including scatter plots and heatmaps, to help identify areas of focus and gaze density.

---

## Features
- **Scatter Plot Visualization**:
  - Displays individual gaze points on a 2D plane.
  - Differentiates gaze progression over time with a color gradient.
- **Heatmap Visualization**:
  - Highlights areas of high gaze concentration using a heatmap.
- **Data Loading**:
  - Reads eye-tracking data from a CSV file.

---

## Technologies Used
- **Python**
  - `pandas`: For data loading and manipulation.
  - `matplotlib`: For creating visualizations.
  - `seaborn`: For enhanced data visualization, including heatmaps.

---

## Prerequisites
1. Python 3.12 or later
2. Required Python libraries:
   - `pandas`
   - `matplotlib`
   - `seaborn`

To install the libraries, run:
```bash
pip install pandas matplotlib seaborn
```

---

## Getting Started
### 1. Clone the Repository
```bash
git clone <repository_url>
cd eye-tracker-processor
```

### 2. Set Up Virtual Environment (Optional)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare Input Data
- Ensure your eye-tracking data is in a CSV file named `simulated_eye_data.csv`.
- Example CSV format:
  ```csv
  timestamp,x_coordinate,y_coordinate
  0.1,200,300
  0.2,210,310
  0.3,220,320
  ```

### 5. Run the Script
```bash
python eye_tracker_processor.py
```

---

## Usage
1. **Scatter Plot**: Displays gaze points on a 2D plane, showing the progression over time.
2. **Heatmap**: Highlights dense areas of gaze activity.

---

## Project Structure
```
project-folder/
|-- eye_tracker_processor.py  # Main script
|-- simulated_eye_data.csv    # Input data file
|-- venv/                     # Virtual environment (optional)
```

---

## Future Enhancements
- Add real-time data processing.
- Integrate with eye-tracking hardware.
- Provide more customization options for visualizations.
