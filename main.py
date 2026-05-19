from src.tracker import init_csv, add_match

def main():
    init_csv()
    
    while True:
        print("\n=== CS2 Match Tracker ===")
        print("1. Добавить матч")
        print("0. Выход")

        choice = input("\nВыбери действие: ").strip()

        if choice == "1":
            add_match()
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неверный ввод, попробуй снова")

if __name__ == "__main__":
    main()