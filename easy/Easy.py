# Чтение файла
with open("inputEasy.txt", "r") as input_file:
    S = input_file.readline().strip()

max_length = 0
current_length = 0

# Перебор всех символов в строке
for ch in S:
    if ch != ' ':  # Если символ не равен ' ', увеличиваем длину текущего слова
        current_length += 1
    else:  # Если символ равен ' '
        if current_length > max_length:
            max_length = current_length  # Обновляем максимальную длину
        current_length = 0  # Сбрасываем длину текущего слова

# Дополнительная проверка на случай, что самым большим словом будет последнее
if current_length > max_length:
    max_length = current_length

# Выводим результат
print("Length of the longest word:", max_length)