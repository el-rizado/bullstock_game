from random import randint


def play():
    number = generate_random()
    score = 100
    bull = 0
    stock = 0
    finish = False
    while not finish:
        guess = int(input("Enter your number : "))
        bull, stock = check(number, guess)
        if bull == 4:
            finish = True
            break
        print(f"bull : {bull}\nstock : {stock}")
        score -= 5
    print(f"You won with {score} scores")


def generate_random():
    flag = False
    out_number = 0
    while not flag:
        number = randint(1000, 9999)
        count_num = 0
        count = {}
        for digit in str(number):
            if digit in count:
                count[digit] += 1
            else:
                count[digit] = 1
        for key in count:
            if count[key] == 1:
                count_num += 1
        if count_num == 4:
            out_number = number
            flag = True
    return out_number

def valid(number):
    if len(str(number)) == 4:
        return True

def check(number, guess):
    bull = 0
    stock = 0
    str_number = str(number)
    str_guess = str(guess)
    for i in range(4):
        if str_guess[i] in str_number:
            if str_guess[i] == str_number[i]:
                bull += 1
            else:
                stock += 1
    return bull, stock

