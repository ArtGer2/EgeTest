#Функция для проверки строки
def is_valid_ip(ip):
    #деление строки на подстроки, разделенных точкой
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    #проверка кождой подстроки на вхождение в диапазон 0 - 255
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True


#Функция для перебора всех строк
def count_valid_ips(file_path):
    valid_ip_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            ip = line.strip()  # Удаляем пробелы и символы новой строки

            if is_valid_ip(ip):
                valid_ip_count += 1
    return valid_ip_count

# Чтение файла
file_path = 'inputMedium.txt'  
# Проверка строк
count = count_valid_ips(file_path)
# Вывод результа
print(f'Valid ip: {count}')