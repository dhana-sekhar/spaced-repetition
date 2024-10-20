# Spaced Repetition Study App

## Overview

The Spaced Repetition Study App is a Streamlit-based application designed to help students and learners manage their study schedule using the spaced repetition technique. This app allows users to log their daily study topics, schedule reviews, and gain insights into their study habits and progress.

## Features

- **Daily Study Logging**: Easily add new topics you've studied each day.
- **Automated Review Scheduling**: The app automatically schedules review sessions based on spaced repetition intervals.
- **Review Tracking**: Mark reviews as completed to keep track of your progress.
- **Insightful Analytics**: 
  - View the distribution of your study topics.
  - Track your review completion rate.
  - Monitor your daily study and revision activity.
  - See your current study and revision streaks.
- **Interactive Charts**: Visualize your study habits and progress with interactive Plotly charts.

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Plotly

## Installation

1. Clone this repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages:

   ```
   pip install streamlit pandas plotly
   ```

## Usage

1. Run the Streamlit app:

   ```
   streamlit run version1.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Use the app:
   - Enter new study topics in the input field and click "Save Study Session".
   - Check off completed reviews in the "Today's Review Schedule" section.
   - Scroll down to view your study insights and progress charts.

## File Structure

- `version1.py`: The main Python script containing the Streamlit app code.
- `study_schedule.csv`: CSV file storing your study data (automatically created when you add your first entry).

## How It Works

1. **Spaced Repetition Algorithm**: The app uses predefined intervals (1, 3, 7, 14, 30, 60, 90, 180, 365, 730 days) for scheduling reviews.
2. **Data Storage**: All study data is stored in a CSV file (`study_schedule.csv`).
3. **Streak Calculation**: The app calculates streaks based on consecutive days of studying and completing reviews.
4. **Insights Generation**: Various charts and metrics are generated to provide visual feedback on your study habits.

## Customization

You can modify the spaced repetition intervals by editing the `intervals` list in the `calculate_review_dates` function within the `version1.py` file.

## Contributing

Contributions to improve the app are welcome. Please feel free to submit issues or pull requests.

## License

This project is open-source and available under the MIT License.

## Support

If you encounter any issues or have questions, please open an issue on the project's GitHub repository.

Happy studying!