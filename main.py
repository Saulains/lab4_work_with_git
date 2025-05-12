import random
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

def get_difficulty():
    print(Fore.CYAN + "Выберите уровень сложности:")
    print("1 - Лёгкий (число от 1 до 10, 5 попыток)")
    print("2 - Средний (число от 1 до 50, 7 попыток)")
    print("3 - Сложный (число от 1 до 100, 10 попыток)")

    while True:
        choice = input(Fore.CYAN + "Ваш выбор: ")
        if choice == '1':
            return 1, 10, 5
        elif choice == '2':
            return 1, 50, 7
        elif choice == '3':
            return 1, 100, 10
        else:
            print(Fore.RED + "Введите 1, 2 или 3.")

def main():
    print(Fore.GREEN + "Добро пожаловать в игру 'Угадай число'!")
    low, high, max_attempts = get_difficulty()
    number = random.randint(low, high)
    attempts = 0
    used_hint = False

    while attempts < max_attempts:
        try:
            guess = int(input(Fore.YELLOW + f"Попытка {attempts + 1}/{max_attempts}. Угадайте число от {low} до {high}: "))
        except ValueError:
            print(Fore.RED + "Пожалуйста, введите целое число.")
            continue

        attempts += 1

        if guess == number:
            print(Fore.GREEN + "Поздравляем! Вы угадали!")
            break
        else:
            print(Fore.RED + "Неправильно.")
            if not used_hint:
                hint_request = input(Fore.YELLOW + "Хотите подсказку? (да/нет): ").lower()
                if hint_request == "да":
                    if guess < number:
                        print(Fore.YELLOW + "Подсказка: Загаданное число больше.")
                    else:
                        print(Fore.YELLOW + "Подсказка: Загаданное число меньше.")
                    used_hint = True
    else:
        print(Fore.RED + f"Вы проиграли. Загаданное число было: {number}")

if __name__ == "__main__":
    main()
