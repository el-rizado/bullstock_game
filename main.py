from random import randint, choice


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
