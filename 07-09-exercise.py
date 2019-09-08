def name_len(name):
    if len(name) < 3:
        print('name must be at least 3 characters')
    elif len(name) > 50:
        print('name can be a maximun of 50 characters')
    else:
        print('name looks good')

#name_len('mad')

# weight Converter
def weight ():
   poid = input('Weight: ')
   poid = int(poid)
   choise = input('(L)bs or (K)g: ')
   l = poid * 0.45
   g = poid / 0.45
   if choise.upper()== 'L':
       print(f"You are {l} kilos")
   elif choise .upper()== 'K':
       print(f"You are {g} pounds")
#weight ()

# while loop

def while_loop():
    i = 1
    while i < 5:
        i = i + 1
        print(f" I am number {i}")
#while_loop()

#while loop guess game
def guess():
    secret_number = 9
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess_count += 1
        guess_num = int(input('Guess: '))
        if guess_num == secret_number:
            print('You win!')
            break
        else:
            print('oh try again')
    else:
        print('sorry, you failed')
guess()