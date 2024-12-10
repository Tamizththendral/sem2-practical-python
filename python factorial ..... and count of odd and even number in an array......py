def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input('enter the number'))
print(f'the factorial is {factorial(num)}')

user_input = input("Enter a list of numbers separated by spaces: ")
l = list(map(int, user_input.split()))
odd = 0
even = 0
for i in l:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even count:", even)
print("Odd count:", odd)
