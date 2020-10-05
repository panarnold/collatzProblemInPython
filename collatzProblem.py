def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number//2
        elif number % 2 == 1:
            number = 3*number + 1
        print(number)
    

def main():
    try:
        num = int(input('give me the number:\n'))
        collatz(num)
    except ValueError:
        print('you need to give me number, not word/words, dummy')
        main()

main()