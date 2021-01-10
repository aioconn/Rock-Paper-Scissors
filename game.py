# Write your code here
import random
name = input('Enter your name:')
print(f'Hello, {name}')
rating = open('rating.txt', 'r')
list1 = rating.read().split()
if name in list1:
    index = list1.index(name)
    score = int(list1[index + 1])
else:
    score = 0
game_type = input()
if game_type == '':
    game_type = 'rock,paper,scissors'
print("Okay, let's start")
game_type_list1 = game_type.split(',')


def wins(guess, comp_choice):
    global score
    global game_type_list1
    guess_index = game_type_list1.index(guess)
    game_type_list2 = game_type_list1[guess_index + 1:] + game_type_list1[:guess_index]
    if guess == comp_choice:
        print(f'There is a draw ({guess})')
        score += 50
    elif comp_choice in game_type_list2[:(int(len(game_type_list2) / 2))]:
        print(f'Sorry, but the computer chose {comp_choice}')
    elif comp_choice in game_type_list2[(int(len(game_type_list2) / 2)):]:
        print(f'Well done. The computer chose {comp_choice} and failed')
        score += 100
    else:
        pass


while True:
    my_guess = input()
    computer_choice = random.choice(game_type_list1)
    if my_guess == '!rating':
        print(f'Your rating: {score}')
        continue
    elif my_guess == '!exit':
        print('Bye!')
        break
    elif my_guess in game_type_list1:
        wins(my_guess, computer_choice)
    else:
        print('Invalid input')

if name in list1:
    index = list1.index(name)
    list1[index + 1] = str(score)
else:
    list1.append(name)
    list1.append(str(score))
rating.close()
my_file = open('rating.txt', 'w')
for i in range(0, len(list1), 2):
    print(list1[i], list1[i+1], file=my_file)
my_file.close()


