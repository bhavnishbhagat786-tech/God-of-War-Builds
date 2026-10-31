
from recommendation_engine import generate_top_equipment

# Temporary test data
equipment = [
    {
        "ID": 1,
        "Title": "Strength Armor",
        "Category": "Chest",
        "Strength": 90,
        "Defence": 30,
        "Runic": 20,
        "Vitality": 40,
        "Cooldown": 20,
        "Luck": 10
    },
    {
        "ID": 2,
        "Title": "Defence Armor",
        "Category": "Chest",
        "Strength": 30,
        "Defence": 90,
        "Runic": 20,
        "Vitality": 90,
        "Cooldown": 20,
        "Luck": 10
    },
    {
        "ID": 3,
        "Title": "Runic Armor",
        "Category": "Chest",
        "Strength": 20,
        "Defence": 30,
        "Runic": 95,
        "Vitality": 40,
        "Cooldown": 80,
        "Luck": 50
    }
]

for style in ["aggressive", "defensive", "runic"]:
    print(f"\n--- {style.upper()} BUILD ---")

    results = generate_top_equipment(
        equipment,
        playstyle=style,
        limit=3
    )

    for item in results:
        print(item)
