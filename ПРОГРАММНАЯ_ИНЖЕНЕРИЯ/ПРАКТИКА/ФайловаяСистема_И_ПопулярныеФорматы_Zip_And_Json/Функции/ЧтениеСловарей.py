import json


# Функция для загрузки данных о стоимости тестов из файла
def load_test_groups(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        scoring_data = json.load(f)

    test_groups = []
    for group in scoring_data["scoring"]:
        required_tests = group["required_tests"]
        group_points = group["points"]
        # Сохраняем список тестов и баллы за группу
        test_groups.append({
            "required_tests": required_tests,
            "group_points": group_points
        })

    return test_groups


# Функция для подсчета итогового количества баллов
def calculate_score(test_groups, results):
    test_results = {i + 1: results[i].strip() == "ok" for i in range(len(results))}

    total_score = 0
    # Проверяем, пройдены ли все тесты в каждой группе
    for group in test_groups:
        all_tests_passed = all(test_results.get(test_num, False) for test_num in group["required_tests"])
        if all_tests_passed:
            total_score += group["group_points"]  # Добавляем баллы, если все тесты пройдены

    return total_score


# Путь к файлу scoring.json
path = "../Тестирование/Файлы_JSON/Тесты_с_Подсчётом.json"

# Загружаем данные о тестовых группах
test_groups = load_test_groups(path)

# Список вердиктов (список "ok" или "wa")
verdicts = [
    "ok", "wa", "ok", "wa", "ok", "ok", "ok", "ok",
    "wa", "wa", "wa", "ok", "wa", "wa", "ok", "wa",
    "wa", "ok", "ok", "ok", "ok", "wa", "ok", "ok",
    "wa", "ok", "wa", "ok", "ok", "ok", "wa", "wa", "ok"
]

# Подсчет итогового количества баллов на основе всех тестов
final_score = calculate_score(test_groups, verdicts)

# Вывод итогового количества баллов
print("Итоговый счет:", final_score)
