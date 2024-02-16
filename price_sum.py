import csv

# Функция для чтения данных из CSV файла и вычисления суммарных затрат для каждой категории потребителей
def calculate_total_spending(filename):
    total_adult = 0
    total_pensioner = 0
    total_child = 0

    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок

        for row in reader:
            total_adult += float(row[1])
            total_pensioner += float(row[2])
            total_child += float(row[3])

    return total_adult, total_pensioner, total_child

# Вызываем функцию и получаем суммарные затраты для каждой категории потребителей
total_adult, total_pensioner, total_child = calculate_total_spending('products.csv')

# Выводим результаты с округлением до двух знаков после десятичной точки
print(f"{total_adult:.2f} {total_pensioner:.2f} {total_child:.2f}")
