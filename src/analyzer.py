import csv
from src.tracker import MATCHES_FILE

def load_matches():
    matches = []
    try:
        with open(MATCHES_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                matches.append({
                    "date": row["date"],
                    "map": row["map"],
                    "result": row["result"],
                    "kills": int(row["kills"]),
                    "deaths": int(row["deaths"]),
                    "assists": int(row["assists"]),
                    "adr": float(row["adr"])
                })
    except FileNotFoundError:
        print("❌ Файл с матчами не найден")
    return matches

def calc_kd(matches):
    total_kills = sum(m["kills"] for m in matches)
    total_deaths = sum(m["deaths"] for m in matches)
    if total_deaths == 0:
        return total_kills
    return round(total_kills / total_deaths, 2)

def calc_winrate(matches):
    if not matches:
        return 0
    wins = sum(1 for m in matches if m["result"] == "win")
    return round((wins / len(matches)) * 100, 1)

def calc_avg_adr(matches):
    if not matches:
        return 0
    return round(sum(m["adr"] for m in matches) / len(matches), 1)

def best_match(matches):
    if not matches:
        return None
    return max(matches, key=lambda m: m["kills"])

def worst_match(matches):
    if not matches:
        return None
    return min(matches, key=lambda m: m["kills"])

def stats_by_map(matches):
    maps = {}
    for m in matches:
        name = m["map"]
        if name not in maps:
            maps[name] = {"wins": 0, "total": 0}
        maps[name]["total"] += 1
        if m["result"] == "win":
            maps[name]["wins"] += 1
    result = {}
    for name, data in maps.items():
        result[name] = round((data["wins"] / data["total"]) * 100, 1)
    return result

def show_stats():
    matches = load_matches()
    if not matches:
        print("❌ Нет данных для анализа. Добавь матчи!")
        return

    print("\n=== 📊 Общая статистика ===")
    print(f"Всего матчей:       {len(matches)}")
    print(f"K/D ratio:          {calc_kd(matches)}")
    print(f"Винрейт:            {calc_winrate(matches)}%")
    print(f"Средний ADR:        {calc_avg_adr(matches)}")

    best = best_match(matches)
    worst = worst_match(matches)
    print(f"\n🏆 Лучший матч:  {best['map']} | {best['kills']}/{best['deaths']}/{best['assists']}")
    print(f"💀 Худший матч:  {worst['map']} | {worst['kills']}/{worst['deaths']}/{worst['assists']}")

    print("\n🗺️  Винрейт по картам:")
    for map_name, winrate in stats_by_map(matches).items():
        print(f"  {map_name}: {winrate}%")