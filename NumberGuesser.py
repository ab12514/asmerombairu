import random

# Asks user to enter an integer
a = input('Enter an integer between 1 and 100: ')

# Handles the case where the number entered is too large
# If the number is not an integer, but within 1 and 100, we simply convert it to an int later on
while int(a)<0 or int(a)>100:
    print('Number entered was too small or too large. Try again.')
    a = input('Enter an integer between 1 and 100: ')

# Makes an array of all possible values
v = []
for x in range(1,101):
    v.insert(x-1,x)

# Asks if number is even
# If not even (odd), we remove all even values. Otherwise, we remove all odd values
b = input('Is your number even? (Input ''yes'' or ''no''): ')
for x in range(1,101):
    if b == 'no':
        if x in v and x%2 == 0:
            v.remove(x)
    else:
        if x in v and x%2 != 0:
            v.remove(x)
print(v)

# Asks if number is strictly below 50
# If no, we cut the left half of the array. Otherwise, we cut the right half
c = input('Is your number below 50? (Input ''yes'' or ''no''): ')
for x in range(1, 101):
    if c == 'no':
        if x in v and x < 50:
            v.remove(x)
            
    else:
        if x in v and x >= 50:
            v.remove(x)
print(v)

# Asks if 5 is a factor 
# If no, we remove any number that is congruent to 0 (mod 5). Otherwise, we remove numbers which aren't congruent to 0 (mod 5)
d = input('Does your number end in 5 or 0? (Input ''yes'' or ''no''): ')
for x in range(1,101):
    if d == 'no':
            if x in v and x%5 == 0:
                v.remove(x)
    else:
        if x in v and x%5 != 0:
            v.remove(x)
           
print(v)

# Pick a random number from our new array
num = random.choice(v)

print('Is your number ' + str(num) + '?')
if num == int(a):
    print('Yeah? Woohoo!')
else:
    print('No? Damn...')



