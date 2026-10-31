from boss_build_engine import generate_boss_build

BOSS = "King Hrolf Kraki"

PLAYSTYLES = [
    "aggressive",
    "defensive",
    "runic",
    "cooldown",
    "survival",
    "balanced"
]

print("\n========== ALGORITHM QUALITY TEST ==========")

for style in PLAYSTYLES:
    result = generate_boss_build(BOSS, playstyle=style)

    if "error" in result:
        print(f"\n❌ {style.upper()}: {result['error']}")
        continue

    equipment = result.get("equipment", {})

    print(f"\nPLAYSTYLE: {style.upper()}")
    print("Build Score:", result.get("build_score"))
    print("Final Score:", result.get("final_score"))

    print("\nRecommended Equipment:")

    for slot, item in equipment.items():
        if isinstance(item, dict) and item.get("Title"):
            print(f"- {slot}: {item['Title']}")

print("\n========== TEST COMPLETED ==========")

from boss_build_engine import generate_boss_build

result = generate_boss_build(
    "King Hrolf Kraki",
    playstyle="aggressive"
)

equipment = result.get("equipment", {})

print("\n===== AGGRESSIVE BUILD DIAGNOSTICS =====")

for slot, item in equipment.items():
    if isinstance(item, dict) and item.get("Title"):
        print("\nSlot:", slot)
        print("Item:", item.get("Title"))
        print("Score:", item.get("Score"))

        for stat in [
            "Strength", "Defence", "Runic",
            "Vitality", "Cooldown", "Luck"
        ]:
            print(stat + ":", item.get(stat, 0))