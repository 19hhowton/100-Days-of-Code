
def add_even_numbers(start, stop):
    sums = 0
    for i in range(start, stop+1):
        if i % 2 == 0:  # if even
            sums += i  # add to the total
    return sums

def add_even_numbers(start, stop):
    sums = 0
    for number in range(2,101,2):
        sums += number

def FizzBuzz(start,stop):
    for i in range(start, stop+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def password_generator(letters, symbols, numbers):
    import random
    import string

    alphabet = list(string.ascii_letters)
    punctuation = list(string.punctuation)

    rand_letters = [random.choice(alphabet) for i in range(0, letters)]
    rand_punctuation = [random.choice(punctuation) for i in range(0, symbols)]
    rand_number = [random.randint(0, 9) for i in range(0, numbers)]
    password = rand_number + rand_punctuation + rand_letters
    random.shuffle(password)
    password = ''.join([str(i) for i in password])
    return f"Your password is: {password}"


if __name__ == '__main__':
    pass
    # print(add_even_numbers(1,100))
    # FizzBuzz(1, 100)
    print(password_generator(12, 2, 5))

