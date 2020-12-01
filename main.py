lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
print("Even numbers from %d to %d are: \n" %(lower, upper))
for number in range(lower, upper+1):
  if(number%2==0):
    print(number)
print("Even numbers from %d to %d are: \n" %(lower, upper))
for number in range(lower, upper+1):
  if(number%2!=0):
    print(number)
