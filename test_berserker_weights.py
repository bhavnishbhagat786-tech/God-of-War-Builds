from database_engine import get_db_connection

connection = get_db_connection()
cursor = connection.cursor(dictionary=True)

try:
    cursor.execute("""
        SELECT *
        FROM berserkers
    """)

    berserkers = cursor.fetchall()

    print("\n========== BERSERKER WEIGHTS ==========")

    for boss in berserkers:
        print("\nBoss:", boss["Name"])
        print("Strength:", boss["Strength_Weight"])
        print("Defence:", boss["Defence_Weight"])
        print("Runic:", boss["Runic_Weight"])
        print("Vitality:", boss["Vitality_Weight"])
        print("Cooldown:", boss["Cooldown_Weight"])
        print("Luck:", boss["Luck_Weight"])

    print("\nTotal Berserkers:", len(berserkers))

finally:
    cursor.close()
    connection.close()