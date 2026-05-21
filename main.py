from src.tracker import init_csv, add_match, delete_match
from src.analyzer import show_stats
from src.visualizer import show_charts

def main():
    init_csv()
    
    while True:
        print("\n=== CS2 Match Tracker ===")
        print("1. Добавить матч")
        print("2. Показать статистику")
        print("3. Показать графики")
        print("4. Удалить матч")
        print("0. Выход")

        choice = input("\nВыбери действие: ").strip()

        if choice == "1":
            add_match()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            show_charts()
        elif choice == "4":
            delete_match()
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неверный ввод, попробуй снова")

if __name__ == "__main__":
    main()