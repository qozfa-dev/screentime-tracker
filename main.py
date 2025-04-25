from src.logger import log_usage
from src.analytics import get_total_usage_today, get_top_apps_today, get_weekly_trend


def print_summary():
    print(f"\nToday's total screen time: {get_total_usage_today()} mins")
    print("Top apps today:")
    for app, mins in get_top_apps_today():
        print(f"  - {app}: {mins} mins")
    print("\nLast 7 days trend:")
    for date, total in get_weekly_trend():
        print(f"  {date}: {total} mins")


if __name__ == "__main__":
    print("1. Log usage\n2. Show summary\n")
    choice = input("Pick option: ")

    if choice == "1":
        app = input("App name: ")
        category = input("Category: ")
        minutes = int(input("Minutes used: "))
        log_usage(app, category, minutes)
        print("Usage logged successfully.")
    elif choice == "2":
        print_summary()
    else:
        print("Invalid option.")
