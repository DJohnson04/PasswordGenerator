import random
#create list to choose random char/symbol/numbers
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num = ['1','2','3','4','5','6','7','8','9','0']
sym = ['!','@','#','$','%','^','&']
site = input('what is the site the password going to be used for? ')
username = input(f'enter {site}\'s username: ')


length = int(input('how long do you want your password to be? '))
password = ''

#adding chars to password at random using import random
while len(password) < length - 2:
    ans = random.randint(1,3)

    if ans == 1:
        if random.randint(1,4) == 3:
            password += abc[random.randint(0,25)].upper()
        else: password += abc[random.randint(0,25)]
    elif ans == 2:
        password += num[random.randint(0,9)]
#adding 2 symbols at the end
for i in range(1,3):
    password += sym[random.randint(0,6)]
#capitalizing the first char of password
password = password.capitalize()
print('the site is ' + site + '\nthe username is: ' + username + '\nthe password is: ' + password )
#creating and editing the new file
with open('./passwordGenerator/passwords.txt', 'a') as f:
    f.write('\nSite: %s Username: %s, password: %s' % (site, username, password))


