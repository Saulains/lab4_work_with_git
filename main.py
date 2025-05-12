import random
import time
from colorama import init, Fore

init(autoreset=True)

def main():
    print(Fore.GREEN + "Добро пожаловать в игру 'Угадай число'!")
    
    # Устанавливаем тайм-аут (например, 30 секунд)
    time_limit = 30
    start_time = time.time()  # Начало отсчета времени

    number = random.randint(1, 100)
    
    print(Fore.YELLOW + f"Угадайте число от 1 до 100. У вас есть {time_limit} секунд.")
    
    attempts = 0
    
    while True:
        # Проверяем, сколько времени прошло
        elapsed_time = time.time() - start_time
        remaining_time = time_limit - elapsed_time
        
        # Если время вышло
        if remaining_time <= 0:
            print(Fore.RED + "Время вышло! Вы не успели угадать.")
            break
        
        # Сообщаем пользователю оставшееся время
        print(Fore.YELLOW + f"Осталось времени: {int(remaining_time)} секунд.")
        
        try:
            guess = int(input(Fore.YELLOW + "Введите число: "))
        except ValueError:
            print(Fore.RED + "Пожалуйста, введите правильное число.")
            continue

        attempts += 1

        if guess == number:
            print(Fore.GREEN + "Поздравляем! Вы угадали число!")
            break
        else:
            print(Fore.RED + f"Вы не угадали. Попробуйте снова.")
    
    print(Fore.YELLOW + f"Вы сделали {attempts} попыток.")

if __name__ == "__main__":
    main()
