
from database_engine import get_db_connection

tables = [
    "armors",
    "axe",
    "blades",
    "spear",
    "shield",
    "rönd",
    "relics",
    "berserkers",
    "final_recommendations"
]

connection = get_db_connection()
cursor = connection.cursor()

try:
    for table in tables:
        print("\n" + "=" * 40)
        print("TABLE:", table.upper())
        print("=" * 40)

        cursor.execute(f"SHOW COLUMNS FROM `{table}`")

        for column in cursor.fetchall():
            print(column[0], "|", column[1])

finally:
    cursor.close()
    connection.close()
