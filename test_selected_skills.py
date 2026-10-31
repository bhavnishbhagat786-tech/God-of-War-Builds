from boss_build_engine import generate_boss_build

result = generate_boss_build("King Hrolf Kraki")

print("\n========== EQUIPMENT SKILLS ==========")

for slot, item in result["equipment"].items():

    if not isinstance(item, dict):
        continue

    print("\nSlot:", slot)
    print("Item:", item.get("Title"))
    print("Skill:", item.get("Skill", "None"))
    print("Perk:", item.get("Perk", "None"))
    print("Application:", item.get("Application", "None"))
    print("Strike:", item.get("Strike", "None"))