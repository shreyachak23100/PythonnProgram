print("Task 1 by Shreya Chakraborty")
#Firsttask
print("First: Sum of two numbers")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum = a+b
print("Sum=", sum) 
print("___________________________")
#Secondtask
print("Second: Odd or Even Checker")
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")
print("___________________________")
#ThirdTask
print("Third: Factorial Calculation")
q = int(input("Enter a number: "))
fact = 1
for i in range(1, q + 1):
    fact = fact * i
print("Factorial =", fact)
print("___________________________")
#FouthTask
print("Fourth: Fibonacci Sequence")
t = int(input("Enter the number of terms: "))
x = 0
y = 1
for i in range(t):
    print(x, end=" ")
    z = x + y
    x = y
    y = z
print("___________________________")   
#Fifthtask
print("Fifth: String Reverse")
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)
print("___________________________")
print("Sixth: Palindrome Check")
s = input("Enter a word: ")
rev = s[::-1]
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
print("___________________________")
print("Seventh: Leap Year Check")
year = int(input("Enter a year: "))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
print("___________________________")
print("Eighth: Armstrong Number")

n = int(input("Enter a number: "))

temp = n
digits = len(str(n))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")





