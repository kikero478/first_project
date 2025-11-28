print('shdksd') 
print('djfskl')
print('sfds')

import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env в окружение
load_dotenv()

def print_author():
    # Дописываем код:
    # 1. Читаем значение переменной окружения 'AUTHOR' с помощью os.getenv()
    # 2. Присваиваем это значение локальной переменной author
    author = os.getenv("AUTHOR")
    
    # Проверка на случай, если переменная не найдена
    if author is None:
        print("Ошибка: Переменная AUTHOR не найдена в окружении.")
        return

    print(f"Автор проекта: {author}")

# Проверяем работу функции
if __name__ == "__main__":
    print_author()
