
from boss_build_engine import generate_boss_build

boss_name = "King Hrolf Kraki"
playstyle = "runic"

result = generate_boss_build(
    boss_name,
    playstyle=playstyle
)

print("\n========== BUILD EXPLANATION TEST ==========")

if "error" in result:
    print("ERROR:", result["error"])

else:
    equipment = result["equipment"]

    print("\nBerserker:", result["berserker"])
    print("Playstyle:", result["playstyle"])
    print("Final Score:", result["final_score"])
    print("Selected equipment:", list(equipment.keys()))
    print("Explanation slots:", list(equipment["explanations"].keys()))
    print("\n========== EQUIPMENT REASONS ==========")

    for slot, reasons in equipment["explanations"].items():

        item = equipment.get(slot)

        if not item or not reasons:
            continue

        print("\n", slot, ":", item.get("Title"))

        for reason in reasons:
            print(
                reason["stat"],
                "| Value:", reason["value"],
                "| Contribution:", reason["contribution"]
            )

    print("\n========== RELIC EXPLANATION ==========")

    print(equipment["relic_explanation"])

    print("\n========== BUILD STRATEGY ==========")

    print(equipment["build_strategy"])

print("\n========== TEST COMPLETED ==========")

from database_engine import get_all_equipment

data = get_all_equipment()

print("\n========== DATABASE CATEGORY CHECK ==========")

for table, items in data.items():

    print("\nTABLE:", table)

    categories = sorted(set(
        str(item.get("Category"))
        for item in items
    ))

    print("Categories:", categories)
    print("Total records:", len(items))