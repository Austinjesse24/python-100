def life_in_weeks(age):
    weeks_in_90_years = 90 * 52
    weeks_lived = age * 52
    weeks_left = weeks_in_90_years - weeks_lived
    
    # Return the message with f-String
    print(f"You have {weeks_left} weeks left.")

# Example test with the hard-coded value from the example
print(life_in_weeks(1))