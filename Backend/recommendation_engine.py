
# ==========================================
# GOD OF WAR - RECOMMENDATION ENGINE 2.0
# ==========================================

PLAYSTYLES = {
    "aggressive": {
        "Strength": 0.40,
        "Defence": 0.10,
        "Runic": 0.20,
        "Vitality": 0.10,
        "Cooldown": 0.10,
        "Luck": 0.10
    },
    "defensive": {
        "Strength": 0.10,
        "Defence": 0.40,
        "Runic": 0.10,
        "Vitality": 0.25,
        "Cooldown": 0.05,
        "Luck": 0.10
    },
    "runic": {
        "Strength": 0.10,
        "Defence": 0.10,
        "Runic": 0.40,
        "Vitality": 0.10,
        "Cooldown": 0.20,
        "Luck": 0.10
    },
    "balanced": {
        "Strength": 0.20,
        "Defence": 0.20,
        "Runic": 0.15,
        "Vitality": 0.15,
        "Cooldown": 0.15,
        "Luck": 0.15
    },
    "cooldown": {
        "Strength": 0.10,
        "Defence": 0.10,
        "Runic": 0.20,
        "Vitality": 0.10,
        "Cooldown": 0.40,
        "Luck": 0.10
    },
    "survival": {
        "Strength": 0.10,
        "Defence": 0.35,
        "Runic": 0.05,
        "Vitality": 0.35,
        "Cooldown": 0.05,
        "Luck": 0.10
    }
}

STATS = [
    "Strength",
    "Defence",
    "Runic",
    "Vitality",
    "Cooldown",
    "Luck"
]


def get_stat(item, stat):
    """Read a stat without depending on SQL column casing."""

    for key, value in item.items():
        if str(key).lower() == stat.lower():
            try:
                return float(value or 0)
            except (TypeError, ValueError):
                return 0.0

    return 0.0


def calculate_equipment_scores(equipment, playstyle="balanced"):
    """Rank equipment using normalized stats and playstyle weights."""

    playstyle = playstyle.lower().strip()

    if playstyle not in PLAYSTYLES:
        raise ValueError(f"Unknown playstyle: {playstyle}")

    if not equipment:
        return []

    weights = PLAYSTYLES[playstyle]

    # Find minimum and maximum values for each stat
    ranges = {}

    for stat in STATS:
        values = [get_stat(item, stat) for item in equipment]
        ranges[stat] = (min(values), max(values))

    results = []

    for item in equipment:
        total_score = 0

        for stat in STATS:
            value = get_stat(item, stat)
            minimum, maximum = ranges[stat]

            # Normalize each stat between 0 and 1
            if maximum == minimum:
                normalized = 0
            else:
                normalized = (value - minimum) / (maximum - minimum)

            total_score += normalized * weights[stat]

        results.append({
            "ID": item.get("ID"),
            "Title": item.get("Title"),
            "Category": item.get("Category"),
            "Score": round(total_score, 4)
        })

    return sorted(
        results,
        key=lambda x: x["Score"],
        reverse=True
    )


def generate_top_equipment(equipment, playstyle="balanced", limit=3):
    """Return the highest-scoring equipment."""

    results = calculate_equipment_scores(
        equipment,
        playstyle
    )

    return results[:limit]
