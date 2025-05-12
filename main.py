import random

import time
from colorama import init, Fore


def get_difficulty():
    difficulty_map = {
        '1': (-10, 10, 5),
        '2': (-50, 50, 7),
        '3': (-100, 100, 10),
        '4': (-2, 10, 5)
    }

    print(Fore.CYAN + "Выберите уровень сложности:")
    print("1 - Лёгкий (число от -10 до 10, 5 попыток)")
    print("2 - Средний (число от -50 до 50, 7 попыток)")
    print("3 - Сложный (число от -100 до 100, 10 попыток)")
    print("4 - Пользовательский")

    while True:
        choice = input(Fore.CYAN + "Ваш выбор: ")
        if choice in difficulty_map:
            if choice == '4':
                low_range = int(input('Введите нижнюю границу:'))
                upper_range = int(input('Введите верхнюю границу:'))
                trials_cnt = int(input('Введите число попыток:'))
                return (low_range, upper_range, trials_cnt)
            else:
                return difficulty_map[choice]
        else:
            print(Fore.RED + "Введите 1, 2, 3 или 4.")

def main():
    print(Fore.GREEN + "Добро пожаловать в игру 'Угадай число'!")
    
    # Устанавливаем тайм-аут (например, 30 секунд)
    time_limit = 30
    start_time = time.time()  # Начало отсчета времени

    # Получаем уровень сложности
    low, high, max_attempts = get_difficulty()
    number = random.randint(low, high)
    
    print(Fore.YELLOW + f"Попробуйте угадать число от {low} до {high}. У вас есть {time_limit} секунд и {max_attempts} попыток.")

    attempts = 0
    hints_left = 1

    while attempts < max_attempts:

        # Проверяем, сколько времени прошло
        elapsed_time = time.time() - start_time
        remaining_time = time_limit - elapsed_time

        # Если время вышло
        if remaining_time <= 0:
            print(Fore.RED + "Время вышло! Вы не успели угадать.")
            break

        # Сообщаем пользователю оставшееся время
        print(Fore.YELLOW + f"Осталось времени: {int(remaining_time)} секунд.")
        
        # Предлагаем ввести либо число, либо нажать h для подсказки
        user_input = input(Fore.YELLOW + f"Попытка {attempts + 1}/{max_attempts}. Введите число для следующей попытки или 'h' для подсказки: ")


        if user_input.lower() == 'h':
            if hints_left > 0:
                print(Fore.CYAN + f"Осталось подсказок: {hints_left}. Загаданное число {'больше' if number > 50 else 'меньше'}.")
                hints_left -= 1
            else:
                print(Fore.RED + "Подсказки закончились!")
            continue

        try:
            guess = int(user_input)
            attempts += 1
            if guess == number:
                print(Fore.GREEN + "Поздравляем! Вы угадали!")
                break
            else:
                print(Fore.RED + f"Вы не угадали. Попробуйте снова.")
        except ValueError:
            print(Fore.RED + "Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
