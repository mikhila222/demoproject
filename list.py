'''x=["guava","mango","lemon"]
print(x)
print(type(x))
x[1]="orange"
print(x)
x.append("jackfriut")
print(x)
x.insert(2,"jackfruit")
print(x)
x.sort()
print(x)
x.sort(reversed.true)
print(x)'''
'''num=int(input("enter a number: "))
def is_prime(num):
    if num<=1:
        return false
    for i in range(2, int(num**0.5) + 1):
         if num % i == 0:
             return False
         return true
if is_prime(num):
  print(num, "is a prime number")
else:
    print(num,"is not a prime number")'''
'''year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")'''
'''num=int(input("enter a number: "))
def is_prime(num):
    if num<=1:
        return false
    for i in range(2, int(num**0.5) + 1):
         if num % i == 0:
             return False
         return true
if is_prime(num):
  print(num, "is a prime number")
else:
    print(num,"is not a prime number") '''
palindrome = lambda string: string == string[::-1]

string = input("Enter a string: ")
if palindrome(string):
  print(string, "is a palindrome")
else:
  print(string, "is not a palindrome")   