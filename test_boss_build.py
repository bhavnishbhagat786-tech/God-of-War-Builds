from boss_build_engine import generate_boss_build

boss_name = "King Hrolf Kraki"

result = generate_boss_build(boss_name)

print("\n========== BOSS BUILD ==========")
print("Boss:", result["berserker"])
print("Build Score:", result["build_score"])

print("\n========== RECOMMENDED EQUIPMENT ==========")

for slot, item in result["equipment"].items():

    if slot == "relic_options":
        print("\nAvailable Relics:", len(item))
        continue

    if item:
        print(
            slot,
            ":", item["Title"],
            "| Score:", item["Score"]
        )
    else:
        print(slot, ": No equipment found")