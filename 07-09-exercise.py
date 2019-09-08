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
#guess()
def cart():
    prices = [10,20,30]
    total = 0
    for item in prices:
        total += item
    print(total)
#cart()

#nested loops

def nested():
    numbers = [5,2,5,2,2]
    for item in numbers:
        print('*' * item)
#nested()

#list

def largest_number():
    array = ['moses', 'Arnaud', 'Issa', 'sebastien', 'Moussa', 'Josephe']
    max = array[0]
    for item in array:
        if len(item) > len(max):
            max = item
    print(max)
#largest_number()

#list matrix

def matrix_list():
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    for row in matrix:
        print(row)
        for item in row:
            print(item)
#matrix_list()

#list methods

def list_methods():
    numbers = [5,2,1,7,4]
    numbers.append(20)
    print(numbers)
    numbers.insert(1,20)
    print(numbers)
    numbers.remove(1)
    print(numbers)
    numbers.pop()
    print(numbers)
    numbers.clear()
    print(numbers)
list_methods()