import random


def computer_number():
    return random.randrange(10)


comp_guess = computer_number()


def evaluate(comp, player):
    if comp > player:
        return 'Too Low!'
    elif comp < player:
        return 'Too High!'
    else:
        return 'Correct!'


def user():
    return input('Please provide a number between 0 and 10. ')


user_guess = user()


def answer(s):
    if s == 'Correct!':
        print(s)
    else:
        print(s)
        answer(evaluate(int(comp_guess), int(user())))


answer(evaluate(int(comp_guess), int(user_guess)))
