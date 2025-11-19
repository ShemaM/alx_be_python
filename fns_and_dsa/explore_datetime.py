from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # return current date for use in part 2

# Part 2: Calculate future date
def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=number_of_days)
    return future_date

# Main program
if __name__ == "__main__":
    current_date = display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(current_date, number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
