
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        if count == 0:
            return 0, 0

        average = total / count

        return total, average

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    except (ValueError, OSError):
        print("Помилка під час читання або обробки файлу")
        return 0, 0


total, average = total_salary("salary_file.txt")

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
