# Screentime Tracker

A Python-based command-line application designed to track and analyze screen time usage across multiple apps. It allows users to log their app usage by category, and provides insights into daily usage patterns, top apps, and trends over time.

## Tools & Technologies Used

- **Python**: Core programming language for the CLI application, handling user input and system logic.
- **SQLite**: Local database to store app usage data, including date, app name, category, and usage duration (in minutes).
- **SQL**: Used for aggregating data (e.g., total screen time) and querying usage trends from the database.
- **CLI (Command Line Interface)**: Allows users to interact with the application through text-based commands.
- **Modular Python Design**: Separated the code into files for better maintainability (`main.py`, `db.py`, `logger.py`, `analytics.py`).

## Features

- **User Input**: Logs app usage by date, app name, category, and minutes spent using the app.
- **Analytics**: Calculates daily total usage and displays the most time-consuming apps.
- **Database**: Uses SQLite to store app usage records and queries trends.
- **Flexibility**: Future integration with a web-based dashboard (to be added).

## Future Improvements

- **Web Application**: Transition from CLI to a fully interactive web application using frameworks like **Flask** or **Django**.
- **Data Visualizations**: Introduce graph-based visualizations (using **Plotly** or **Matplotlib**) to show trends in screen time, breakdown by category, and user goals.
- **Advanced Analytics**: Incorporate machine learning models to predict usage trends and offer personalized recommendations.
- **User Authentication**: Allow users to create accounts and track screen time across different devices.
- **Goals & Alerts**: Set daily usage goals and send alerts when users exceed their screen time limit.
  
## Setup
### 1. Clone the repository:
```bash
git clone https://github.com/qozfa-dev/screentime-tracker.git
cd screentime-tracker
```
### 2. Run the application
```bash
python main.py
```

## Future Dependencies

In the future, when adding additional features (e.g., Flask for the web application, or Matplotlib/Plotly for visualizations), a `requirements.txt` will be created to manage dependencies.

## License

MIT.


