from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date(days: int):
    future_date = datetime.now() + timedelta(days=days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()
    days = int(input("Enter Number of days: "))
    calculate_future_date(days)

if __name__ == "__main__":
    main()