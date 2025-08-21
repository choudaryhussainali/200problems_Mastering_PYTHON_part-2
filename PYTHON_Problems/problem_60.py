# Enter your age in years: 20
# You are approximately 240 months old.
# You are approximately 7300 days old.

# Function to calculate and display age in months and days
def calculate_age_in_units():
    """
    Prompts the user for their age in years, then calculates and prints
    their approximate age in months and days.
    """
    try:
        # Get age in years from the user
        age_years_str = input("Enter your age in years: ")
        age_years = int(age_years_str)

        # Basic validation for a reasonable age
        if age_years < 0 or age_years > 120:
            print("Please enter a realistic age.")
            return

        # Calculate age in months (approximately 12 months per year)
        age_months = age_years * 12

        # Calculate age in days (approximately 365 days per year, ignoring leap years for simplicity)
        age_days = age_years * 365

        # Print the results
        print(f"You are approximately {age_months} months old.")
        print(f"You are approximately {age_days} days old.")

    except ValueError:
        print("Invalid input. Please enter a whole number for your age.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to run the age calculator
calculate_age_in_units()


# ----------------------------------------
# Author: Choudary Hussain Ali
# GitHub: https://github.com/choudaryhussainali
# LinkedIn: https://linkedin.com/in/ch-hussain-ali
# ----------------------------------------
