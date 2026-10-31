from boss_build_engine import generate_boss_build
from database_engine import get_db_connection

connection = get_db_connection()
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT Name FROM berserkers")
bosses = cursor.fetchall()

cursor.close()
connection.close()

print("\n========== ALL BOSS BUILDS ==========")

for boss in bosses:

    boss_name = boss["Name"]

    result = generate_boss_build(boss_name)

    print("\nBoss:", boss_name)

    if "error" in result:
        print(result["error"])
        continue

    print("Build Score:", result["build_score"])
    print("Final Score:", result["final_score"])

    for slot, item in result["equipment"].items():

        if isinstance(item, dict) and "Title" in item:
            print(
                slot, ":",
                item["Title"],
                "| Score:",
                item.get("Score", 0)
            )

    print("Synergy Score:", result["equipment"]["synergy_score"])