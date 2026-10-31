
from database_engine import recommend_armors

styles = [
    "aggressive",
    "defensive",
    "runic",
    "balanced"
]

for style in styles:
    print(f"\n===== {style.upper()} =====")

    try:
        results = recommend_armors(style, limit=3)

        for item in results:
            print(
                item["Title"],
                "| Category:", item["Category"],
                "| Score:", item["Score"]
            )

    except Exception as error:
        print("ERROR:", error)
