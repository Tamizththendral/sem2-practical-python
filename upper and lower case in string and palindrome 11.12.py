a=input('enter the sting:')
low=0
upp=0
for i in a:
    if  i.islower():
        low+=1
    elif i.isupper():
        upp+=1
print(f'lowercase:{low}\nuppercase:{upp}')

a=input('enter the string')
b=a[::-1]
print(f'reversed string{b}')
if a==b:
    print('palindrome')
else:
    print('not palindrome')
