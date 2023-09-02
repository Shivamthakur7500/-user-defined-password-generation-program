import string
import random
n=int(input('how many terms do you want in your password:'))
def password(n):
    letter1=int(input('Do you want Lowrcase letters in your password ? \n 1-YES\n 2-NO: '))
    letter2=int(input('Do you want uppercase letters in your password ? \n 1-YES\n 2-NO: '))
    digit=int(input('Do you want Digits  in your password ? \n 1-YES\n 2-NO: '))
    special_char=int(input('Do you want special_char in your password ? \n 1-YES\n 2-NO: '))
    if letter1==1:
        lettera=string.ascii_lowercase
    else:
        print('')
    if letter2==1:
       letterb=string.ascii_letters
    else:
        print('')
    if digit==1:
        digit1=string.digits
    else:
        print('')
    if special_char==1:
        special_char1=string.punctuation
    else:
        print('ok')
    if (letter1==1,letter2==1,digit==1,special_char==1):
       result=''.join(random.choice(lettera+string.ascii_letters+digit1+string.punctuation)for i in range(n))
       print('Your generated passwrd is :',result)
    else:
        print('sorry invalid choices\ntry again later')
password(n)
