import csv
import os
from datetime import date

MATCHES_FILE = "data/matches.csv"

MAPS = [
    "Mirage", "Dust2", "Inferno", "Nuke",
    "Ancient", "Anubis", "Vertigo"
]

def init_csv():
    if not os.path.exists(MATCHES_FILE) or os.path.getsize(MATCHES_FILE) == 0:
        with open(MATCHES_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "map", "result", "kills", "deaths", "assists", "adr"])

def get_int(prompt, min_val=0, max_val=999):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  Введи число от {min_val} до {max_val}")
        except ValueError:
            print("  Ошибка: введи целое число")

def get_map():
    print("\nДоступные карты:")
    for i, m in enumerate(MAPS, 1):
        print(f"  {i}. {m}")
    while True:
        try:
            choice = int(input("Выбери карту (номер): "))
            if 1 <= choice <= len(MAPS):
                return MAPS[choice - 1]
            print(f"  Введи число от 1 до {len(MAPS)}")
        except ValueError:
            print("  Ошибка: введи номер карты")

def get_result():
    while True:
        result = input("Результат (win/loss): ").strip().lower()
        if result in ["win", "loss"]:
            return result
        print("  Введи win или loss")

def add_match():
    print("\n=== Добавить матч ===")
    match_map = get_map()
    result = get_result()
    kills = get_int("Убийства: ")
    deaths = get_int("Смерти: ")
    assists = get_int("Помощи: ")
    adr = get_int("Средний урон за раунд (ADR): ", 0, 500)

    if deaths == 0:
        print("  ⚠️  Смертей 0 — K/D будет считаться как максимальный")

    with open(MATCHES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date.today(), match_map, result, kills, deaths, assists, adr])

    print("\n✅ Матч успешно добавлен!")

def show_matches():
    matches = []
    with open(MATCHES_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            matches.append(row)

    if not matches:
        print("❌ Нет сохранённых матчей")
        return matches

    print("\n=== Список матчей ===")
    for i, m in enumerate(matches, 1):
        print(f"{i}. {m['date']} | {m['map']} | {m['result']} | "
              f"K/D: {m['kills']}/{m['deaths']}/{m['assists']} | ADR: {m['adr']}")
    return matches

def delete_match():
    matches = show_matches()
    if not matches:
        return

    while True:
        try:
            choice = int(input("\nВведи номер матча для удаления (0 — отмена): "))
            if choice == 0:
                print("Отмена удаления")
                return
            if 1 <= choice <= len(matches):
                removed = matches.pop(choice - 1)
                with open(MATCHES_FILE, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=["date", "map", "result", "kills", "deaths", "assists", "adr"])
                    writer.writeheader()
                    writer.writerows(matches)
                print(f"\n✅ Матч удалён: {removed['date']} | {removed['map']} | {removed['result']}")
                return
            print(f"  Введи число от 1 до {len(matches)}")
        except ValueError:
            print("  Ошибка: введи целое число")