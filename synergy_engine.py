SYNERGY_KEYWORDS = {
    "realm_shift": [
        "realm shift", "nine realms"
    ],
    "stun": [
        "stun", "stun damage", "shockwave"
    ],
    "defence": [
        "protection", "defensive", "blocking",
        "parrying", "shield"
    ],
    "cooldown": [
        "cooldown", "refresh"
    ],
    "elemental": [
        "bifröst", "bifrost", "poison",
        "shock", "sonic", "elemental"
    ],
    "rage": [
        "rage"
    ],
    "healing": [
        "healing", "health", "restoring"
    ],
    "damage": [
        "melee damage", "increased damage",
        "damage"
    ]
}



SYNERGY_WEIGHTS = {
    "realm_shift": 1.5,
    "stun": 1.2,
    "defence": 1.0,
    "cooldown": 1.2,
    "elemental": 1.2,
    "rage": 1.0,
    "healing": 1.2,
    "damage": 1.0
}


def analyze_synergy(equipment):
    matched = {}
    synergy_score = 0.0

    for slot, item in equipment.items():

        if not isinstance(item, dict):
            continue

        description = " ".join([
            str(item.get("Skill", "")),
            str(item.get("Perk", "")),
            str(item.get("Application", "")),
            str(item.get("Strike", "")),
            str(item.get("Effect", ""))
        ]).lower()

        for synergy, keywords in SYNERGY_KEYWORDS.items():

            if any(keyword in description for keyword in keywords):
                matched.setdefault(synergy, []).append({
                    "slot": slot,
                    "item": item.get("Title")
                })

    # Reward matching effects across different equipment slots
    for synergy, items in matched.items():

        unique_slots = {
            item["slot"] for item in items
        }

        slot_count = len(unique_slots)

        if slot_count >= 2:
            extra_slots = slot_count - 1
            weight = SYNERGY_WEIGHTS.get(synergy, 1.0)

            synergy_score += extra_slots * weight

    synergy_score = round(min(synergy_score, 5.0), 4)

    return {
        "synergies": matched,
        "synergy_score": synergy_score
    }
