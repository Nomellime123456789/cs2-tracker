import matplotlib.pyplot as plt
from src.analyzer import load_matches, calc_kd, stats_by_map

def chart_kd_over_time(matches):
    if len(matches) < 2:
        print("❌ Нужно минимум 2 матча для графика")
        return

    kd_values = []
    for i in range(1, len(matches) + 1):
        kd_values.append(calc_kd(matches[:i]))

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(matches) + 1), kd_values, marker="o", color="cyan", linewidth=2)
    plt.axhline(y=1.0, color="red", linestyle="--", label="K/D = 1.0")
    plt.title("K/D Ratio по матчам")
    plt.xlabel("Матч")
    plt.ylabel("K/D Ratio")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def chart_winrate_by_map(matches):
    map_stats = stats_by_map(matches)
    if not map_stats:
        print("❌ Нет данных для графика")
        return

    maps = list(map_stats.keys())
    winrates = list(map_stats.values())
    colors = ["green" if w >= 50 else "red" for w in winrates]

    plt.figure(figsize=(10, 5))
    plt.bar(maps, winrates, color=colors)
    plt.axhline(y=50, color="white", linestyle="--", label="50%")
    plt.title("Винрейт по картам")
    plt.xlabel("Карта")
    plt.ylabel("Винрейт (%)")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, axis="y")
    plt.tight_layout()
    plt.show()

def show_charts():
    matches = load_matches()
    if not matches:
        print("❌ Нет данных для графиков. Добавь матчи!")
        return

    print("\n=== 📈 Графики ===")
    print("1. K/D по матчам")
    print("2. Винрейт по картам")

    choice = input("\nВыбери график: ").strip()

    if choice == "1":
        chart_kd_over_time(matches)
    elif choice == "2":
        chart_winrate_by_map(matches)
    else:
        print("Неверный ввод")