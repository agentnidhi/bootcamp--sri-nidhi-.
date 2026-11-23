#compound interest calculator 

principle = 0
time = 0
rate = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Please enter a valid principle amount greater than 0.")

while time <=0:
    time = float(input("Enter the time period: "))
    if time <= 0:
        print("Please enter a valid time period greater than 0.")

while rate <=0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Please enter a valid rate of interest greater than 0.")

compound_interest = round(principle * (pow(1 + rate / 100, time)),2)
print(f"The compound interest is: {compound_interest}")