def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            
            for line in file:
                line = line.strip().split(",") 
                if len(line) != 3:
                    print(f"Попередження: Некоректні дані у рядку: '{line}'")
                    continue
                id, name, age = line[0], line[1], line[2]
                cats_info.append({
                    "id": id,
                    "name": name,
                    "age": age
                })
            return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)