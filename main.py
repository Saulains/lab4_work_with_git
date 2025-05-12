import random
from colorama import init, Fore

init(autoreset=True)

def main():
    print(Fore.GREEN + "Добро пожаловать в игру 'Угадай число'!")
    number = random.randint(1, 100)
    guess = int(input(Fore.YELLOW + "Угадайте число от 1 до 100: "))
    
    if guess == number:
        print(Fore.GREEN + "Поздравляем! Вы угадали!")
    else:
        print(Fore.RED + f"Вы не угадали. Было число {number}")

if __name__ == "__main__":
    main()
