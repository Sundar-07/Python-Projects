"""
The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, 
then dividing the answer again by their height
"""

Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))

Height = Height/100

print("Height is: ",Height)

BMI = Weight / (Height * Height)

print("Your Body Mass Index is: ",BMI)

if(BMI > 0):
	if(BMI <= 16):
		print("You are severely underweight")
	elif(BMI <= 18.5):
		print("You are underweight")
	elif(BMI <= 25):
		print("You are Healthy")
	elif(BMI <= 30):
		print("You are overweight")
	else: print("You are severely overweight")
else:("Enter valid details")