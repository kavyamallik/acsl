print("enter your age:")
age_str = input()
age = int(age_str)
if age < 13: 
    print ("You are a kid.")
elif age < 20:
    print("You are a teen.")
else:
    print("You are an adult since your age is " + str(age))