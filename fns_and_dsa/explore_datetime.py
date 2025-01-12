from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    # Prompt the user for input
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the number of days to the current date
    future_date = datetime.now() + timedelta(days=number_of_days)
    
    # Print the future date in a readable format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()  # Display the current date and time
    calculate_future_date()     # Calculate and display the future date

if __name__ == "__main__":
    main()
