print("welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age < 12:
        bill = 5
        print("Child ticket $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket $7.")
    else:
        bill = 12
        print("Adult ticket $12.")
        
    wants_photo = input("Do you want a photo taken? Y for yes or N for no. ").strip().upper()
    if wants_photo == "Y":
        # Add $3 to the bill
        bill = bill + 3 #bill += 3   
        
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
    