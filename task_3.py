
import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def print_directory_structure(directory, prefix=""):
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (not item.is_dir(), item.name.lower())
        )

        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1

            connector = "└── " if is_last else "├── "

            if entry.is_symlink():
                print(prefix + connector + Fore.GREEN + entry.name)

            elif entry.is_dir():
                print(prefix + connector + Fore.BLUE + entry.name + "/")

                new_prefix = prefix + ("    " if is_last else "│   ")

                print_directory_structure(entry, new_prefix)

            else:
                print(prefix + connector + Fore.GREEN + entry.name)

    except PermissionError:
        print(prefix + Fore.RED + "Немає доступу до директорії")

    except OSError as error:
        print(prefix + Fore.RED + f"Помилка: {error}")


def main():
    if len(sys.argv) != 2:
        print("Використання: python task_3.py <шлях_до_директорії>")
        return

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + "Помилка: директорія не існує")
        return

    if not directory.is_dir():
        print(Fore.RED + "Помилка: вказаний шлях не є директорією")
        return

    print(Fore.BLUE + directory.name + "/")
    print_directory_structure(directory)


if __name__ == "__main__":
    main()
