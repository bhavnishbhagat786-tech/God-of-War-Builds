from database_engine import get_all_equipment

equipment = get_all_equipment()

print("\n========== EQUIPMENT CATEGORIES ==========")

for table, items in equipment.items():
    print(f"\n{table.upper()}")

    if not items:
        print("No records")
        continue

    if "Category" in items[0]:
        categories = set(
            item["Category"] for item in items
            if item["Category"]
        )
        print("Categories:", sorted(categories))
    else:
        print("No Category column")

    print("Total records:", len(items))

print("\n========== COMPLETED ==========")