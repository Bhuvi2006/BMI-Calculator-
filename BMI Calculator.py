'''Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more'''
print("***WELCOME***")
input("Enter your name: ")
h=float(input("Enter your height(in cm): "))
w=float(input("Enter your weight(in kgs): "))
bmi=w/(h/100)**2
print("Your BMI is: ",int(bmi))
if bmi>=18.5 and bmi<25:
    print("Normal, You are healthy!!!")
elif bmi<18.5:
    print("Under weight")
elif bmi>=25 and bmi<30:
    print("Over weight... Try to eat healthy!")
elif bmi>=30:
    print("Obesity... Avoid eating junk ")
print("Have a nice day!!!")
