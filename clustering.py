import mysql.connector
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def cluster_armours():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Kratos@123",
        database="gow_armors"
    )

    try:
        # Load armour data from MySQL
        df = pd.read_sql(
            "SELECT * FROM armors",
            conn
        )

        stat_columns = [
            "Strength",
            "Defence",
            "Runic",
            "Vitality",
            "Cooldown",
            "Luck"
        ]

        # Convert stats to numeric values
        for column in stat_columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

        # Replace missing values with zero
        df[stat_columns] = (
            df[stat_columns].fillna(0)
        )

        # Standardize the equipment stats
        scaler = StandardScaler()

        X = scaler.fit_transform(
            df[stat_columns]
        )

        # Train the K-Means model
        model = KMeans(
            n_clusters=3,
            random_state=42,
            n_init=10
        )

        df["Cluster"] = model.fit_predict(X)

        print("\n===== ARMOUR CLUSTERS =====\n")

        print(
            df[
                ["Title", "Strength", "Defence", "Cluster"]
            ].sort_values("Cluster").to_string(index=False)
        )

        print("\n===== CLUSTER STATISTICS =====\n")

        print(
            df.groupby("Cluster")[stat_columns]
            .mean()
            .round(2)
        )

        return df

    finally:
        conn.close()


if __name__ == "__main__":
    cluster_armours()
