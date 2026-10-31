
from database_engine import generate_armour_build

playstyles = [
    "aggressive",
    "defensive",
    "runic",
    "balanced",
    "cooldown",
    "survival"
]

for style in playstyles:

    print("\n==============================")
    print("PLAYSTYLE:", style.upper())
    print("==============================")

    build = generate_armour_build(style)

    for item in build["equipment"]:
        print(
            item["Category"],
            ":", item["Title"],
            "| Score:", item["Score"]
        )

    print("Overall Score:", build["total_score"])
