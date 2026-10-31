from database_engine import get_db_connection, get_all_equipment
from relic_engine import recommend_relic
from synergy_engine import analyze_synergy


STATS = [
    "Strength",
    "Defence",
    "Runic",
    "Vitality",
    "Cooldown",
    "Luck"
]


PLAYSTYLE_WEIGHTS = {
    "balanced": {
        "Strength": 0.167, "Defence": 0.167,
        "Runic": 0.167, "Vitality": 0.167,
        "Cooldown": 0.166, "Luck": 0.166
    },
    "aggressive": {
        "Strength": 0.50, "Defence": 0.05,
        "Runic": 0.20, "Vitality": 0.05,
        "Cooldown": 0.10, "Luck": 0.10
    },
    "defensive": {
        "Strength": 0.05, "Defence": 0.40,
        "Runic": 0.05, "Vitality": 0.35,
        "Cooldown": 0.10, "Luck": 0.05
    },
    "runic": {
        "Strength": 0.10, "Defence": 0.05,
        "Runic": 0.50, "Vitality": 0.05,
        "Cooldown": 0.25, "Luck": 0.05
    },
    "cooldown": {
        "Strength": 0.10, "Defence": 0.10,
        "Runic": 0.15, "Vitality": 0.05,
        "Cooldown": 0.50, "Luck": 0.10
    },
    "survival": {
        "Strength": 0.05, "Defence": 0.45,
        "Runic": 0.05, "Vitality": 0.35,
        "Cooldown": 0.05, "Luck": 0.05
    }
}

SLOTS = {
    "armors": ["Chest", "Waist", "Wrist"],
    "axe": ["Grip", "Knob", "Maul"],
    "blades": ["Handles", "Pommels"],
    "spear": ["Hind", "Sauroter"]
}


def get_berserker(name):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM berserkers WHERE Name = %s",
            (name,)
        )
        return cursor.fetchone()

    finally:
        cursor.close()
        connection.close()


def get_stat(item, stat):
    for key, value in item.items():
        if key.lower() == stat.lower():
            return float(value or 0)

    return 0.0


def calculate_boss_score(items, weights):
    

    if not items:
        return []

    scores = []

    for item in items:
        score = 0

        for stat in STATS:
            values = [get_stat(x, stat) for x in items]

            minimum = min(values)
            maximum = max(values)
            current = get_stat(item, stat)

            if maximum == minimum:
                normalized = 1 if maximum > 0 else 0
            else:
               normalized = (current - minimum) / (maximum - minimum)

            weight = float(weights.get(stat, 0))
            score += normalized * weight

        result = item.copy()
        result["Score"] = round(score, 4)
        scores.append(result)

    return sorted(
        scores,
        key=lambda x: x["Score"],
        reverse=True
    )


def explain_equipment_choice(item, candidates, weights):

    if not item or not candidates:
        return []

    contributions = []

    for stat in STATS:

        values = [get_stat(x, stat) for x in candidates]

        minimum = min(values)
        maximum = max(values)
        current = get_stat(item, stat)

        if maximum == minimum:
            normalized = 1 if maximum > 0 else 0
        else:
            normalized = (current - minimum) / (maximum - minimum)

        weight = float(weights.get(stat, 0))
        contribution = normalized * weight

        contributions.append({
            "stat": stat,
            "value": current,
            "weight": round(weight, 4),
            "contribution": round(contribution, 4)
        })

    contributions.sort(
        key=lambda x: x["contribution"],
        reverse=True
    )

    return contributions[:3]


def explain_relic_choice(relic, playstyle, weights):

    if not relic:
        return {
            "reason": "No relic recommendation available.",
            "effect": None,
            "focus_stats": []
        }

    effect = relic.get("Effect") or relic.get("Overview") or "Effect details unavailable."

    focus_stats = sorted(
        weights.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return {
        "reason": f"Selected for the {playstyle} build based on its relic ranking.",
        "effect": effect,
        "focus_stats": [
            {
                "stat": stat,
                "weight": round(weight, 4)
            }
            for stat, weight in focus_stats
        ]
    }


def generate_build_strategy(playstyle):

    strategies = {
        "balanced": "Maintain a balance between damage, defence and abilities.",
        "aggressive": "Focus on dealing high damage and defeating enemies quickly.",
        "defensive": "Focus on defence, protection and surviving powerful attacks.",
        "runic": "Focus on Runic attacks and ability-based damage.",
        "cooldown": "Focus on reducing ability cooldowns and using attacks frequently.",
        "survival": "Prioritize defence, vitality and staying alive during combat."
    }

    return strategies.get(
        playstyle,
        "Use a balanced combat approach."
    )


def generate_boss_build(boss_name, playstyle="balanced"):

    boss = get_berserker(boss_name)

    if not boss:
        return {"error": "Berserker not found"}

    # Validate playstyle
    playstyle = playstyle.lower().strip()

    if playstyle not in PLAYSTYLE_WEIGHTS:
        return {"error": "Invalid playstyle"}

    # Original Berserker weights
    boss_weights = {
        "Strength": float(boss["Strength_Weight"]),
        "Defence": float(boss["Defence_Weight"]),
        "Runic": float(boss["Runic_Weight"]),
        "Vitality": float(boss["Vitality_Weight"]),
        "Cooldown": float(boss["Cooldown_Weight"]),
        "Luck": float(boss["Luck_Weight"])
    }

    # Selected Playstyle weights
    style_weights = PLAYSTYLE_WEIGHTS[playstyle]

    # Combine Berserker + Playstyle weights
    weights = {
        stat: (
            boss_weights[stat] * 0.60
            + style_weights[stat] * 0.40
        )
        for stat in STATS
    }

    equipment = get_all_equipment()
    build = {}
    build_explanations = {}


    # 1. Select best armour and weapons
    for table, categories in SLOTS.items():

        for category in categories:

            items = [
                item for item in equipment[table]
                if str(item.get("Category", "")).strip().lower()
                == category.lower()
            ]

            ranked = calculate_boss_score(items, weights)

            build[category] = ranked[0] if ranked else None

            selected_item = build[category]

            build_explanations[category] = explain_equipment_choice(
                selected_item,
                items,
                weights
            )

    # 2. Select shield and rond
    for table in ["shield", "rond"]:

        ranked = calculate_boss_score(
            equipment[table],
            weights
        )

        build[table] = ranked[0] if ranked else None

        selected_item = build[table]

        build_explanations[table] = explain_equipment_choice(
            selected_item,
            equipment[table],
            weights
        )


    # 3. Calculate equipment score
    selected_items = [
        item for item in build.values()
        if isinstance(item, dict) and "Score" in item
    ]

    equipment_score = (
        sum(item["Score"] for item in selected_items)
        / len(selected_items)
        if selected_items else 0
    )

    # 4. Recommend best relic
    ranked_relics = recommend_relic(
        equipment["relics"],
        weights
    )

    build["relic"] = (
        ranked_relics[0] if ranked_relics else None
    )

    build["relic_explanation"] = explain_relic_choice(
    build["relic"],
    playstyle,
    weights
)

    build["build_strategy"] = generate_build_strategy(playstyle)

    build["relic_options"] = ranked_relics

    # 5. Analyze synergy
    synergy_result = analyze_synergy(build)
    synergy_score = synergy_result["synergy_score"]

    # 6. Relic score
    relic_score = (
        build["relic"]["Score"]
        if build.get("relic") else 0
    )

    # 7. Final combined score
    final_score = (
        (equipment_score * 0.70) +
        (relic_score * 0.20) +
        (min(synergy_score, 5) / 5 * 0.10)
    )

    # 8. Save scores and selected playstyle
    build["synergy"] = synergy_result["synergies"]
    build["synergy_score"] = synergy_score
    build["equipment_score"] = round(equipment_score, 4)
    build["relic_score"] = round(relic_score, 4)
    build["final_score"] = round(final_score, 4)
    build["playstyle"] = playstyle
    build["explanations"] = build_explanations

    return {
        "berserker": boss_name,
        "playstyle": playstyle,
        "equipment": build,
        "build_score": round(equipment_score, 4),
        "final_score": round(final_score, 4)
    }

build_explanations = {}