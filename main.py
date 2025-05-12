import random
from colorama import Fore

def get_difficulty():
    difficulty_map = {
        '1': (1, 10, 5),
        '2': (1, 50, 7),
        '3': (1, 100, 10),
    }

    print(Fore.CYAN + "Выберите уровень сложности:")
    print("1 - Лёгкий (число от 1 до 10, 5 попыток)")
    print("2 - Средний (число от 1 до 50, 7 попыток)")
    print("3 - Сложный (число от 1 до 100, 10 попыток)")

    while True:
        choice = input(Fore.CYAN + "Ваш выбор: ")
        if choice in difficulty_map:
            return difficulty_map[choice]
        else:
            print(Fore.RED + "Введите 1, 2 или 3.")

def main():
    print(Fore.CYAN + "Добро пожаловать в игру 'Угадай число'!")
    
    low, high, max_attempts = get_difficulty()
    number = random.randint(low, high)
    attempts = 0
    hints_left = 1  # Начальное количество подсказок

    print(Fore.YELLOW + f"Попробуйте угадать число от {low} до {high}. У вас {max_attempts} попыток.")
    
    while attempts < max_attempts:
        # Предлагаем ввести либо число, либо нажать h для подсказки
        user_input = input(Fore.YELLOW + f"Попытка {attempts + 1}/{max_attempts}. Введите число для следующей попытки или 'h' для подсказки: ")

        # Если введено 'h', показываем подсказку
        if user_input.lower() == 'h':
            if hints_left > 0:
                print(Fore.CYAN + f"Осталось подсказок: {hints_left}. Загаданное число {'больше' if number > guess else 'меньше'}.")
                hints_left -= 1
            else:
                print(Fore.RED + "Подсказки закончились!")
            continue

        # Если введено число, проверяем
        try:
            guess = int(user_input)
        except ValueError:
            print(Fore.RED + "Пожалуйста, введите целое число.")
            continue

        attempts += 1

        if guess == number:
            print(Fore.GREEN + "Поздравляем! Вы угадали число!")
            break
        else:
            print(Fore.RED + f"Неверно! Загаданное число {'больше' if guess < number else 'меньше'}.")

            if hints_left > 0:
                print(Fore.YELLOW + f"Осталось подсказок: {hints_left}. Чтобы получить подсказку, нажмите 'h'.")

            if attempts == max_attempts:
                print(Fore.RED + f"Вы проиграли. Загаданное число было {number}. Попробуйте снова!")

if __name__ == "__main__":
    main()
