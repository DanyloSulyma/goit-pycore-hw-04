print("HELLO WORLD")
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Попередження: Некоректні дані у рядку: '{line}'")
                    continue
            
            if count == 0:
                return (0, 0)
            
            average = total / count
            return (total, average)

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася непередбачена помилка: {e}")
        return (0, 0)

total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")