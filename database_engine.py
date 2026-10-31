
import mysql.connector
from recommendation_engine import generate_top_equipment


def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Kratos@123",
        database="gow_armors"
    )


def get_armors():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT ID, Title, Category,
                   Strength, Defence, Runic,
                   Vitality, Cooldown, Luck
            FROM armors
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        connection.close()


def generate_armour_build(playstyle="balanced"):
    armors = get_armors()

    if not armors:
        return {
            "playstyle": playstyle,
            "equipment": [],
            "total_score": 0
        }

    # Separate armour into categories
    categories = {}

    for armour in armors:
        category = armour.get("Category")

        if not category:
            continue

        categories.setdefault(category, []).append(armour)

    build = []

    # Select the best item from every category
    for category, items in categories.items():

        result = generate_top_equipment(
            items,
            playstyle=playstyle,
            limit=1
        )

        if result:
            build.append(result[0])

    average_score = (
        sum(item["Score"] for item in build) / len(build)
        if build else 0
    )

    return {
        "playstyle": playstyle,
        "equipment": build,
        "total_score": round(average_score, 4)
    }

EQUIPMENT_TABLES = {
    "armors": "armors",
    "axe": "axe",
    "blades": "blades",
    "spear": "spear",
    "shield": "shield",
    "rond": "rönd",
    "relics": "relics"
}


def get_all_equipment():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    equipment_data = {}

    try:
        for key, table_name in EQUIPMENT_TABLES.items():
            cursor.execute(f"SELECT * FROM `{table_name}`")
            equipment_data[key] = cursor.fetchall()

        return equipment_data

    finally:
        cursor.close()
        connection.close()