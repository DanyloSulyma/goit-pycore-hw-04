import sys
from colorama import init, Fore, Style
from pathlib import Path
init()

def visualize_tree(path, level=0):
    try: 
        directory = Path(path)
        indent = "  " * level
        for item in sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name)):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}{Fore.RESET}")
                visualize_tree(item, level + 1)
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}❌ Доступ заборонено: {path.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{indent}{Fore.RED}❌ Помилка при читанні {path.name}: {e}{Style.RESET_ALL}")
def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії.")
    else:
        path = Path(sys.argv[1])
        if not path.exists():
            print("Помилка: Шлях не існує.")
        elif not path.is_dir():
            print("Помилка: Це не директорія.")
        else:
            visualize_tree(path)

if __name__ == "__main__":
    main()