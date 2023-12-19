# find sum of numbers from 1 to a given number20
print("Enter a number")
last_number_str = input()
last_number = int(last_number_str)

sum = 0
for i in range(1,last_number + 1):
    sum = sum + i

print ("The sum is: " + str(sum) )
