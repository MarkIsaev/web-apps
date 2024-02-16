n = int(input())  # Считываем количество участников
results = list(map(int, input().split()))  # Считываем результаты участников и преобразуем в список целых чисел

# Сортируем результаты в порядке убывания
results.sort(reverse=True)

# Ищем второй максимальный результат, пропуская возможные повторения
second_place_score = None
for score in results:
    if score < results[0]:
        second_place_score = score
        break

print(second_place_score)
