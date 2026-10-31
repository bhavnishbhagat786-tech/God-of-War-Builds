from database_engine import get_all_equipment

equipment = get_all_equipment()

print("\n========== EQUIPMENT DATABASE TEST ==========")

for category, items in equipment.items():
    print(f"\n{category.upper()}: {len(items)} records")

    if items:
        print("Columns:", list(items[0].keys()))
        print("First item:", items[0].get("Title"))

print("\n========== TEST COMPLETED ==========")