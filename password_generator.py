import random

print('GENERATOR HASEŁ !')


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'


number = input('Liczba haseł? -> ')
number = int(number)

length = input('Długość hasła? ->')
length = int(length)

print('\nOto wygenerowane hasło/hasła:')


for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)

  print(password)