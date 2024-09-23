def find_unpaired_cube(file_path):
    count = {}

    # Читаем данные из файла
    with open(file_path, 'r') as file:
        data = file.read().split()  # Убираем лишние пробелы и разделяем по пробелам

    # Подсчитываем количество вхождений каждого кубика
    for num_str in data:
        num = int(num_str)  # Преобразуем строку в число
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Находим кубик, который встречается нечетное количество раз
    for num, cnt in count.items():
        if cnt % 2 != 0:
            return num  # Возвращаем число без пары


file_path = 'inputHard.txt' 
unpaired_cube = find_unpaired_cube(file_path)
print(f'Кубик без пары: {unpaired_cube}')