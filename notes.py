
'''name = input('enter your name: ')
phrase = 'your name is ' + name
print(phrase)
print(phrase.replace('name', 'age').upper())
print(phrase.index('y'))
print(phrase[1])
print(len(phrase) - 1)

numbers = [42, 4, 8, 15, 16, 23]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']
friends.extend(numbers)
friends.append('Puficu')
friends.insert(1, 'Odin') or friends[1] = 'Odin
friends.remove('Toby')
#friends.clear()
friends.pop()
print(friends.index('Kevin'))
print(friends.count('Jim'))
numbers.sort()
friends.reverse()

friends2 = friends.copy

def sub(num):
    return 3 - num

is_male = True
is_tall = True

if is_male and is_tall:
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are male but not tall')
elif not(is_male) and is_tall:
    print('you are not male but tall')
else:
    print('you are not male and not tall')

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

num1 = float(input('Enter first number: '))
op = input('Enter operator: ')
num2 = float(input('Enter second number: '))

if op == '+':
    print('Your result is: ' + str(num1 + num2))
elif op == '-':
    print('Your result is: ' + str(num1 - num2))
elif op == '/':
    print('Your result is: ' + str(num1 / num2))
elif op == '*':
    print('Your result is: ' + str(num1 * num2))
else:
    print('Invalid operator.')

monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
}

print(monthConversions.get('luv', 'not valid'))

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

def game(secret_word):

    guess = ''
    guess_count = 0
    guess_limit = 3
    out_of_guesses = False

    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
         guess = input('Enter guess: ')
         guess_count += 1
        else:
         out_of_guesses = True

    if out_of_guesses:
        print('Out of guesses.')
    else:
        print('You win.')


print('Cine-i cel mai cute?')
game('puficu')

friends = ['pifi', 'pifidus', 'chiutus']

for name in range(2):
    print(friends[name])

for index in range(5):
    if index == 0:
        print('first')
    else:
        print('not first')

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))


nume = input('what is your name? ')
varsta = input('how old are you? ')
print('you have ' + str(100 - int(varsta)) + ' years left to live.')

list = [[1, 2], [3, 4], [5, 6]]
names = [['andreea', 'eu'], ['singrid', 'emilia'], ['ana', 'bianca']]
for pair in list:
    print(pair[0])
for number in list[0]:
    print(number)
for letter in names[0][1]:
        print(letter)
phrase = names[2][0] + ' are mere.'
print(phrase.replace(names[2][0], 'bogdan'))

lista_cu_liste = [
    ['icre', 1.5],
    ['avocado', 3],
    ['cirese', 10]
]
for list in lista_cu_liste:
    print('pretul pentru ' + list[0] + ' este ' + str(list[1]))
        '''