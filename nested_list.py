def find_second_highest_score(students):
    sorted_students = sorted(students, key=lambda x: x[1])  # Сортируем учеников по возрастанию оценок
    unique_scores = sorted(set(score for name, score in sorted_students))

    if len(unique_scores) < 2:
        return None  # No second highest score if less than 2 students

    return unique_scores[1]


def get_names_with_score(students, score):
    names = set()  # Используем множество для хранения уникальных имен
    for name, student_score in students:
        if student_score == score:
            names.add(name)
    return sorted(names)  # Возвращаем список имен, отсортированный в алфавитном порядке


def main():
    N = int(input())

    students = []
    for _ in range(N):
        name = input()
        score = float(input())
        students.append([name, score])

    second_highest_score = find_second_highest_score(students)

    if second_highest_score is None:
        print("No second highest score")
    else:
        names = get_names_with_score(students, second_highest_score)
        print("\n".join(sorted(names)))


if __name__ == "__main__":
    main()
