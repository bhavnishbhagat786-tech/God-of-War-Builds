from analytics import get_data_science_insights
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from analytics import get_analytics
from flask import Flask, request, jsonify, render_template
import requests
import mysql.connector
from boss_build_engine import generate_boss_build
from boss_build_engine import generate_boss_build, PLAYSTYLE_WEIGHTS
from database_engine import get_db_connection

app = Flask(__name__, static_folder="static")

# ---------------- Camera Route ----------------

@app.route("/pen-control")
def pen_control():
    return render_template("pen_control.html")

@app.route("/hand-gesture")
def hand_gesture():
    return render_template("hand_gesture.html")

# ---------------- DATABASE CONNECTION ----------------

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Kratos@123",
        database="gow_armors"
    )




# ---------------- HOME PAGE ----------------

@app.route("/")
def home():
    return app.send_static_file("index.html")



# ---------------- BUILD RECOMMENDATION API ----------------

@app.route("/api/build", methods=["GET"])
def get_build():

    name = request.args.get("berserker", "").strip()
    playstyle = request.args.get("playstyle", "balanced").strip().lower()

    if not name:
        return jsonify({
            "error": "Berserker name is required"
        }), 400

    try:
        # Generate build using Berserker and selected Playstyle
        result = generate_boss_build(
            name,
            playstyle=playstyle
        )

        if "error" in result:
            return jsonify(result), 404

        equipment = result["equipment"]

        def get_title(slot):
            item = equipment.get(slot)

            if isinstance(item, dict):
                return item.get("Title")

            return None

        def combine_titles(slots):
            parts = []

            for slot in slots:
                title = get_title(slot)

                if title:
                    parts.append(title)

            return " + ".join(parts) if parts else None

        response = {
            "Berserker": result["berserker"],
            "Playstyle": result["playstyle"],
            "Build_Score": result["build_score"],

            "Chest": get_title("Chest"),
            "Wrist": get_title("Wrist"),
            "Waist": get_title("Waist"),

            "Axe": combine_titles(["Grip", "Knob", "Maul"]),
            "Blades": combine_titles(["Handles", "Pommels"]),
            "Spear": combine_titles(["Hind", "Sauroter"]),

            "Shield": get_title("shield"),
            "Rond": get_title("rond"),
            "Relic": get_title("relic"),

            "Final_Score": result["final_score"],
            "Equipment_Score": equipment["equipment_score"],
            "Relic_Score": equipment["relic_score"],
            "Synergy_Score": equipment["synergy_score"],
            "Synergies": equipment["synergy"],

            "Equipment_Details": equipment
        }

        return jsonify(response)

    except Exception as error:
        app.logger.exception("Dynamic build generation failed")

        return jsonify({
            "error": str(error)
        }), 500


# ---------------- AI CONNECTION TEST ----------------

@app.route("/api/ai-test", methods=["GET"])
def ai_test():
    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "prompt": (
                    "You are the God of War Ragnarök Build Assistant. "
                    "Greet the user in one friendly sentence."
                ),
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        data = response.json()

        return jsonify({
            "reply": data.get("response", "")
        })

    except requests.RequestException:
        app.logger.exception("Ollama connection failed")
        return jsonify({
            "error": "AI is unavailable. Check whether Ollama is running."
        }), 503


# ---------------- AI CHAT API ----------------

GOW_LORE = {
    "who is kratos": (
        "Kratos is the main protagonist of the God of War series. "
        "He is a Spartan warrior who becomes the Greek God of War "
        "and later travels through the Norse realms."
    ),
    "who is atreus": (
        "Atreus is Kratos and Faye's son. He is also known as Loki "
        "and plays a major role in God of War Ragnarök."
    ),
    "who is faye": (
        "Faye, also known as Laufey, is Kratos's wife in the Norse saga "
        "and Atreus's mother."
    ),
    "who is mimir": (
        "Mimir is a wise figure known for his knowledge of Norse mythology. "
        "He accompanies Kratos and Atreus on many of their adventures."
    ),
    "who is thor": (
        "Thor is the Norse God of Thunder, a son of Odin, "
        "and an important character in God of War Ragnarök."
    ),
    "who is odin": (
        "Odin is the All-Father and ruler of the Aesir gods "
        "in the Norse God of War saga."
    ),
    "who is freya": (
        "Freya is a powerful Vanir goddess who becomes an important "
        "ally of Kratos after their earlier conflict."
    ),
    "who is bald ur": (
        "Baldur is Odin's son and a major antagonist in God of War (2018)."
    ),
    "who is baldur": (
        "Baldur is Odin's son and a major antagonist in God of War (2018)."
    ),
    "who is fenrir": (
        "Fenrir is a giant wolf who plays an important role "
        "in God of War Ragnarök."
    ),
    "what is ragnarok": (
        "Ragnarök is a series of catastrophic events in Norse mythology "
        "associated with the destruction and renewal of the world."
    ),
    "what is leviathan axe": (
        "The Leviathan Axe is Kratos's frost-infused weapon in the Norse saga. "
        "Faye originally owned it before it came into Kratos's possession."
    ),
    "what are blades of chaos": (
        "The Blades of Chaos are chained blades associated with Kratos's "
        "Greek past. He continues to use them in the Norse saga."
    ),
    "who is brok": (
        "Brok is a Dwarf blacksmith who helps Kratos and Atreus "
        "by crafting and upgrading equipment."
    ),
    "who is sindri": (
        "Sindri is a Dwarf blacksmith and Brok's brother. "
        "He helps Kratos and Atreus throughout their journey."
    ),
    "who is tyr": (
        "Týr is the Norse god associated with war and a major figure "
        "in God of War Ragnarök."
    ),
    "who is heimdall": (
        "Heimdall is an Aesir god in God of War Ragnarök, "
        "known for his extraordinary perception."
    ),
    "who is surtur": (
        "Surtr is a fire giant associated with the events of Ragnarök."
    ),
    "who is ang rboda": (
        "Angrboda is a Jötunn girl who becomes important to Atreus's story."
    ),
    "who is angrboda": (
        "Angrboda is a Jötunn girl who becomes important to Atreus's story."
    ),
    "who is the wife of kratos in greek mythalogy": (
        "Lsandra is the wife of kratos on greek mythology."
    )
}

@app.route("/api/ai-chat", methods=["POST"])
def ai_chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({
            "error": "Message must be text."
        }), 400

    message = message.strip()

    if not message:
        return jsonify({
            "error": "Please enter a message."
        }), 400

    if len(message) > 2000:
        return jsonify({
            "error": "Message is too long."
        }), 400
        
        

    # Find a Berserker name mentioned in the user's message.
    conn = None
    cursor = None
    build = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM final_recommendations"
        )
        all_builds = cursor.fetchall()

        for row in all_builds:
            berserker_name = row.get("Berserker", "")

            if berserker_name and berserker_name.lower() in message.lower():
                build = row
                break

    except mysql.connector.Error:
        app.logger.exception("AI database lookup failed")
        return jsonify({
            "error": "Could not access the build database."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

    # Give the AI verified build information when a Berserker is identified.
    if build:
        database_context = (
            "Verified build data retrieved from the project's MySQL database:\n"
            f"Berserker: {build.get('Berserker')}\n"
            f"Build Score: {build.get('Build_Score')}\n"
            f"Chest: {build.get('Chest')}\n"
            f"Wrist: {build.get('Wrist')}\n"
            f"Waist: {build.get('Waist')}\n"
            f"Axe: {build.get('Axe')}\n"
            f"Blades: {build.get('Blades')}\n"
            f"Spear: {build.get('Spear')}\n"
            f"Shield: {build.get('Shield')}\n"
            f"Rond: {build.get('Rond')}\n"
            f"Relic: {build.get('Relic')}\n"
        )
    else:
        database_context = (
            "No matching Berserker build was found for this message. "
            "Do not claim that you retrieved a build from the database. "
            "If the user wants a specific recommended build, ask which "
            "Berserker they are fighting and ask them to use the exact name "
            "from the website's Berserker dropdown."
        )

    system_prompt = (
        "You are Kratos AI, a knowledgeable assistant specializing in "
        "God of War (2005), God of War II, God of War III, God of War (2018), "
        "and God of War Ragnarök.\n\n"

        "IDENTITY AND BEHAVIOR:\n"
        "- Answer questions accurately, clearly, and directly.\n"
        "- Be friendly and answer in the same language as the user when possible.\n"
        "- Never invent characters, relationships, events, weapons, or abilities.\n"
        "- If you do not know a fact, admit uncertainty instead of guessing.\n"
        "- Distinguish confirmed game lore from fan theories.\n"
        "- Do not confuse characters with similar names.\n\n"

        "VERIFIED NORSE SAGA CHARACTER FACTS:\n"
        "- Kratos's second wife is Faye, also known as Laufey.\n"
        "- Kratos and Faye's son is Atreus.\n"
        "- Atreus is also known as Loki.\n"
        "- Freya is a separate character from Faye.\n"
        "- Freya was previously married to Odin.\n"
        "- Atreus is Kratos's son, not his brother.\n\n"

        "GOD OF WAR LORE RULES:\n"
        "- When asked about family relationships, identify the characters carefully.\n"
        "- When asked about a particular game, answer according to that game's story.\n"
        "- Do not present speculation as an established fact.\n"
        "- These example facts are not a complete lore database. "
        "If uncertain about other details, say so.\n\n"

        "BUILD RECOMMENDATION RULES:\n"
        "- Use the supplied MySQL database context as the source of truth "
        "for this project's verified equipment recommendations.\n"
        "- Never invent, rename, or silently replace equipment listed in the database.\n"
        "- Do not claim that a build was retrieved from the database if no "
        "matching build was found.\n"
        "- The Build Score is the score calculated by this project, not a "
        "guaranteed probability of winning in the game.\n"
        "- If a requested build is missing, explain that the database did "
        "not provide a matching build.\n\n"

        "DATABASE CONTEXT:\n"
        + database_context
    
    )

    try:
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2:1b",
                "system": system_prompt,
                "prompt": message,
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        ai_data = response.json()

        return jsonify({
            "reply": ai_data.get("response", "").strip()
        })

    except requests.RequestException:
        app.logger.exception("Ollama chat request failed")
        return jsonify({
            "error": "AI is unavailable. Check whether Ollama is running."
        }), 503


# ---------------- RUN FLASK ----------------

# analystics route 
@app.route("/analytics")
def analytics():
    try:
        data = get_analytics()
        return render_template("analytics.html", data=data)
    except Exception as e:
        app.logger.exception("Analytics dashboard error")
        return f"Analytics error: {e}", 500
    

# cluster route
@app.route("/clustering")
def clustering_dashboard():
    return render_template("clustering.html")

#cluster Api
@app.route("/api/clustering")
def clustering_api():
    conn = None

    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Kratos@123",
            database="gow_armors",
            connection_timeout=5
        )

        df = pd.read_sql("SELECT * FROM armors", conn)

        if df.empty:
            return jsonify({"error": "No armour records found."}), 404

        stat_columns = [
            "Strength", "Defence", "Runic",
            "Vitality", "Cooldown", "Luck"
        ]

        for column in stat_columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        df[stat_columns] = df[stat_columns].fillna(0)

        if len(df) < 3:
            return jsonify({
                "error": "At least 3 armour records are required for clustering."
            }), 400

        scaler = StandardScaler()
        X = scaler.fit_transform(df[stat_columns])

        model = KMeans(n_clusters=3, random_state=42, n_init=10)
        df["Cluster"] = model.fit_predict(X)

        statistics = (
            df.groupby("Cluster")[stat_columns]
            .mean()
            .round(2)
            .to_dict(orient="index")
        )

        counts = df["Cluster"].value_counts().to_dict()

        # Ensure all three cluster labels exist in the response.
        statistics = {
            str(i): statistics.get(i, {col: 0 for col in stat_columns})
            for i in range(3)
        }
        counts = {str(i): int(counts.get(i, 0)) for i in range(3)}

        # Convert NumPy/Pandas values to regular JSON-compatible values.
        armours = df[
            ["Title", "Strength", "Defence", "Runic", "Vitality", "Cluster"]
        ].copy()

        armours["Cluster"] = armours["Cluster"].astype(int)
        armours = armours.astype(object).where(pd.notna(armours), None)

        return jsonify({
            "armours": armours.to_dict(orient="records"),
            "statistics": statistics,
            "counts": counts
        })

    except Exception as error:
        app.logger.exception("Clustering API failed")
        return jsonify({"error": str(error)}), 500

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
      
      # cluster api conect to armors anda database
      
@app.route("/api/armours")
def get_armours():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Kratos@123",
            database="gow_armors",
            connection_timeout=5
        )

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                ID, Title, Strength, Defence,
                Runic, Vitality, Cooldown, Luck
            FROM armors
            ORDER BY Title
        """)

        armours = cursor.fetchall()

        # Convert missing or NULL stat values to zero.
        stat_columns = [
            "Strength", "Defence", "Runic",
            "Vitality", "Cooldown", "Luck"
        ]

        for armour in armours:
            for column in stat_columns:
                armour[column] = float(armour[column] or 0)

        return jsonify(armours)

    except Exception as error:
        app.logger.exception("Armour API failed")
        return jsonify({"error": str(error)}), 500

    finally:
        if conn is not None and conn.is_connected():
            conn.close()      

#comparison route
@app.route("/compare")
def compare_page():
    return render_template("compare.html")

# data scinece doute 
@app.route("/api/data-science-insights")
def data_science_insights_api():
    try:
        insights = get_data_science_insights()
        return jsonify(insights)
    except Exception:
        app.logger.exception("Data Science Insights API failed")
        return jsonify({
            "error": "Could not load Data Science insights. Check the Flask terminal."
        }), 500

@app.route("/insights")
def insights_page():
    return render_template("insights.html")


@app.route("/api/build-evaluation")
def build_evaluation_api():
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM final_recommendations
            ORDER BY Build_Score DESC
        """)

        builds = cursor.fetchall()
# Convert Saved_At into local-time compatible string
        for build in builds:
            if build.get("Saved_At"):
                build["Saved_At"] = build["Saved_At"].strftime(
            "%Y-%m-%dT%H:%M:%S"
        )

        if not builds:
            return jsonify({
                "error": "No recommended builds found."
            }), 404
    
        scores = [
            float(build["Build_Score"] or 0)
            for build in builds
        ]

        result = {
            "total_builds": len(builds),
            "average_score": round(
                sum(scores) / len(scores), 4
            ),
            "highest_score": max(scores),
            "lowest_score": min(scores),
            "best_build": builds[0],
            "builds": builds
        }

        return jsonify(result)

    except Exception:
        app.logger.exception("Build evaluation failed")

        return jsonify({
            "error": "Could not load build evaluation."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()
            
# flask route 
@app.route("/evaluation")
def evaluation_page():
    return render_template("evaluation.html")

# friequency route
@app.route("/api/equipment-frequency")
def equipment_frequency_api():
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        columns = [
            "Chest", "Wrist", "Waist", "Axe", "Blades",
            "Spear", "Shield", "Rond", "Relic"
        ]

        result = {}

        for column in columns:
            query = f"""
                SELECT `{column}` AS equipment, COUNT(*) AS frequency
                FROM final_recommendations
                WHERE `{column}` IS NOT NULL
                  AND TRIM(`{column}`) != ''
                GROUP BY `{column}`
                ORDER BY frequency DESC, equipment ASC
            """

            cursor.execute(query)
            result[column] = cursor.fetchall()

        return jsonify(result)

    except Exception:
        app.logger.exception("Equipment frequency analysis failed")
        return jsonify({
            "error": "Could not load equipment frequency data."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if conn is not None:
            conn.close()

@app.route("/equipment-frequency")
def equipment_frequency_page():
    return render_template("equipment_frequency.html")


@app.route("/api/compare-builds", methods=["GET"])

@app.route("/api/compare-builds", methods=["GET"])
def compare_builds():
    try:
        playstyle = request.args.get(
            "playstyle", "balanced"
        ).strip().lower()

        if playstyle not in PLAYSTYLE_WEIGHTS:
            return jsonify({
                "error": "Invalid playstyle"
            }), 400

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT Name FROM berserkers")
        bosses = cursor.fetchall()

        cursor.close()
        connection.close()

        comparisons = []

        for boss in bosses:
            result = generate_boss_build(
                boss["Name"],
                playstyle=playstyle
            )

            if "error" in result:
                continue

            equipment = result["equipment"]

            comparisons.append({
                "Berserker": result["berserker"],
                "Playstyle": playstyle,
                "Equipment_Score": result["build_score"],
                "Final_Score": result["final_score"],
                "Relic": (
                    equipment.get("relic") or {}
                ).get("Title", "N/A"),
                "Synergy_Score": equipment.get(
                    "synergy_score", 0
                )
            })

        comparisons.sort(
            key=lambda item: item["Final_Score"],
            reverse=True
        )

        return jsonify({
            "playstyle": playstyle,
            "total_berserkers": len(comparisons),
            "best_build": (
                comparisons[0] if comparisons else None
            ),
            "comparisons": comparisons
        })

    except Exception as error:
        app.logger.exception("Comparison failed")
        return jsonify({"error": str(error)}), 500

# ---------------- final reccomendation ----------------
@app.route("/api/save-build", methods=["POST"])
def save_build():
    data = request.get_json()

    if not data or not data.get("Berserker"):
        return jsonify({"error": "Invalid build data"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO final_recommendations
            (Berserker, Build_Score, Chest, Wrist, Waist,
             Axe, Blades, Spear, Shield, Rond, Relic)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data.get("Berserker"),
            data.get("Build_Score"),
            data.get("Chest"),
            data.get("Wrist"),
            data.get("Waist"),
            data.get("Axe"),
            data.get("Blades"),
            data.get("Spear"),
            data.get("Shield"),
            data.get("Rond"),
            data.get("Relic")
        ))

        connection.commit()

        return jsonify({
            "success": True,
            "message": "Build saved successfully!",
            "id": cursor.lastrowid
        })

    except Exception as error:
        connection.rollback()
        return jsonify({"error": str(error)}), 500

    finally:
        cursor.close()
        connection.close()

# save data builds history

@app.route("/api/saved-builds", methods=["GET"])
def get_saved_builds():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT *
            FROM final_recommendations
            ORDER BY ID DESC
        """)

        builds = cursor.fetchall()

        return jsonify({
            "success": True,
            "total": len(builds),
            "builds": builds
        })

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        cursor.close()
        connection.close()
       
# delete button 
@app.route("/api/delete-build/<int:build_id>", methods=["DELETE"])
def delete_build(build_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM final_recommendations WHERE ID = %s",
            (build_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({
                "success": False,
                "error": "Build not found."
            }), 404

        connection.commit()

        return jsonify({
            "success": True,
            "message": "Build deleted successfully!"
        })

    except Exception as error:
        connection.rollback()
        return jsonify({"error": str(error)}), 500

    finally:
        cursor.close()
        connection.close()       
          
if __name__ == "__main__":
    app.run(debug=True)

