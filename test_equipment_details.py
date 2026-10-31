from database_engine import get_all_equipment

equipment = get_all_equipment()

for category in ["shield", "rond", "relics"]:
    print("\n==========", category.upper(), "==========")

    for item in equipment[category]:
        print("\n", item)