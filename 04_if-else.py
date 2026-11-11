email = input("Enter email: ")
password = input("Enter password: ")

if email == 'new@mail.com' and password == 'pass@123':
    print('Welcome user')
elif email == 'new@mail.com'and password == 'pass@123':
    print('Incorrect password')
    password=  input('Enter passsword again:')
    if password=='pass@123':
        print('now correct')
    else:
        print('again incorrect')
else:
    print('Invalid email')

