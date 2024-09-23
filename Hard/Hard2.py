def find_unpaired_cube(file_path):
    result = 0

    # Читаем данные из файла
    with open(file_path, 'r') as file:
        data = file.read().split()  # разделяем по пробелам

    # Применяем XOR для нахождения непарного кубика
    for num_str in data:
        num = int(num_str)
        result ^= num  # Применяем XOR

    return result  # Возвращаем число без пары

file_path = 'inputHard.txt'
unpaired_cube = find_unpaired_cube(file_path)
print(f'Кубик без пары: {unpaired_cube}')