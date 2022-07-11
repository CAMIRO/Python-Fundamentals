# Dia 11

#1. it will loop through all the letters the string has: 
for i in 'holla la playa when you see me on the streets':
    print('letter', end=' ')



#2. this could check it an email is valid:
email =False

for i in 'juan@myemail.com':
    if(i=="@"):
        email = True

if email:
    print('email valid')
else:
    print('email invalid',)


# 3. Range Loop 
for i in range(5):
    print(i, end=' ')