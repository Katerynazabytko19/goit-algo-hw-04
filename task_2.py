
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    raise ValueError("Неправильний формат рядка")

                cat_id, name, age = parts

                if not cat_id.strip() or not name.strip() or not age.strip():
                    raise ValueError("Відсутні дані про кота")

                cat = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }

                cats.append(cat)

    except FileNotFoundError:
        print("Файл не знайдено")
        return []

    except (ValueError, OSError):
        print("Помилка під час читання або обробки файлу")
        return []

    return cats


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
