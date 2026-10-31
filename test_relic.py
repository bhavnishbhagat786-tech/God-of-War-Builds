from database_engine import get_all_equipment
from boss_build_engine import get_berserker
from relic_engine import recommend_relic

boss_name = "King Hrolf Kraki"

boss = get_berserker(boss_name)

weights = {
    "Strength": boss["Strength_Weight"],
    "Defence": boss["Defence_Weight"],
    "Runic": boss["Runic_Weight"],
    "Vitality": boss["Vitality_Weight"],
    "Cooldown": boss["Cooldown_Weight"],
    "Luck": boss["Luck_Weight"]
}

equipment = get_all_equipment()

ranked_relics = recommend_relic(
    equipment["relics"],
    weights
)

print("\n====== BEST RELICS FOR", boss_name, "======")

for relic in ranked_relics:
    print(
        relic["Title"],
        "| Profile:", relic["Profile"],
        "| Score:", relic["Score"]
    )

print("\nBEST RELIC:", ranked_relics[0]["Title"])