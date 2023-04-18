import random
import string

# Создаем список символов, из которых будут генерироваться пароли
# В данном случае используем цифры, заглавные и строчные буквы и несколько специальных символов
symbols = string.digits + string.ascii_letters + '!@#$%^&*()3s1W2R3y4q5o6p8z'

# Создаем пустой список для хранения паролей
passwords = []

# Генерируем 10 паролей от 8 до 16 символов
for i in range(1003):
    # Генерируем случайную длину пароля от 8 до 16 символов
    password_length = random.randint(8, 16)

    # Генерируем пароль, выбирая случайные символы из списка symbols
    password = ''.join([random.choice(symbols) for _ in range(password_length)])

    # Добавляем пароль в список passwords
    passwords.append(password)
# Проверяем, есть ли такой пароль уже в списке passwords


if password not in passwords:
    # Если пароля еще нет в списке, добавляем его
    passwords.append(password)
# Открываем файл для записи
with open('passwords.txt', 'w') as file:
    # Записываем каждый пароль в файл на отдельной строке
    for password in passwords:
        file.write(password + '\n')

print('Пароли сохранены в файл passwords.txt')
