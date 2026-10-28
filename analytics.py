
import mysql.connector
import pandas as pd

def get_analytics():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Kratos@123",
        database="gow_armors"
    )

    try:
        # Load existing equipment data
        armors = pd.read_sql(
            "SELECT * FROM armors", conn
        )

        axes = pd.read_sql(
            "SELECT * FROM axe", conn
        )

        blades = pd.read_sql(
            "SELECT * FROM blades", conn
        )

        spears = pd.read_sql(
            "SELECT * FROM spear", conn
        )

        relics = pd.read_sql(
            "SELECT * FROM relics", conn
        )

        # Equipment counts
        equipment_counts = {
            "Armours": len(armors),
            "Axes": len(axes),
            "Blades": len(blades),
            "Spears": len(spears),
            "Relics": len(relics)
        }

        # Armour statistics
        stat_columns = [
            "Strength",
            "Defence",
            "Runic",
            "Vitality",
            "Cooldown",
            "Luck"
        ]

        available_stats = [
            col for col in stat_columns
            if col in armors.columns
        ]

        stats = (
            armors[available_stats]
            .apply(pd.to_numeric, errors="coerce")
            .mean()
            .round(2)
            .to_dict()
        )

        # Top 10 armours by Strength
        top_armours = []

        if "Strength" in armors.columns:
            top = armors.copy()

            top["Strength"] = pd.to_numeric(
                top["Strength"], errors="coerce"
            )

            top = top.nlargest(10, "Strength")

            top_armours = top[
                ["Title", "Strength"]
            ].fillna(0).to_dict(orient="records")

        return {
            "total_equipment": sum(
                equipment_counts.values()
            ),
            "equipment_counts": equipment_counts,
            "average_stats": stats,
            "top_armours": top_armours
        }

    finally:
        conn.close()

  
if __name__ == "__main__":
    import json

    print(json.dumps(
        get_analytics(),
        indent=4,
        default=str
    ))

# datascince function
def get_data_science_insights():
    import pandas as pd
    import mysql.connector

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Kratos@123",
        database="gow_armors"
    )

    try:
        df = pd.read_sql("SELECT * FROM armors", conn)

        if df.empty:
            return {"error": "No armour data found."}

        stats = [
            "Strength", "Defence", "Runic",
            "Vitality", "Cooldown", "Luck"
        ]

        for column in stats:
            df[column] = pd.to_numeric(
                df[column], errors="coerce"
            ).fillna(0)

        insights = {
            "total_armours": int(len(df)),
            "average_stats": df[stats].mean().round(2).to_dict(),
            "highest_strength": df.loc[
                df["Strength"].idxmax(), "Title"
            ],
            "highest_defence": df.loc[
                df["Defence"].idxmax(), "Title"
            ],
            "highest_runic": df.loc[
                df["Runic"].idxmax(), "Title"
            ]
        }

        return insights

    finally:
        conn.close()
        
        

      