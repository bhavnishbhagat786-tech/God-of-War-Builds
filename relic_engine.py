RELIC_PROFILES = {
    "melee": {
        "Strength": 0.8, "Runic": 0.1, "Luck": 0.1
    },
    "stun": {
        "Strength": 0.35, "Runic": 0.45,
        "Vitality": 0.1, "Luck": 0.1
    },
    "bifrost": {
        "Runic": 0.7, "Strength": 0.2, "Luck": 0.1
    },
    "realm_shift": {
        "Cooldown": 0.5, "Runic": 0.25, "Luck": 0.25
    },
    "runic": {
        "Cooldown": 0.7, "Runic": 0.3
    },
    "defence": {
        "Defence": 0.6, "Vitality": 0.4
    },
    "sonic": {
        "Strength": 0.4, "Runic": 0.4, "Luck": 0.2
    },
    "poison": {
        "Runic": 0.5, "Strength": 0.3, "Cooldown": 0.2
    },
    "shock": {
        "Runic": 0.4, "Strength": 0.4, "Cooldown": 0.2
    },
    "damage": {
        "Strength": 0.6, "Runic": 0.3, "Luck": 0.1
    },
    "soul": {
        "Strength": 0.35, "Runic": 0.35,
        "Vitality": 0.15, "Luck": 0.15
    }
}


def get_relic_profile(effect):
    effect = str(effect).lower()

    if "realm shift" in effect:
        return "realm_shift"

    if "runic cooldown" in effect:
        return "runic"

    if "bifröst" in effect or "bifrost" in effect:
        return "bifrost"

    if "sonic" in effect:
        return "sonic"

    if "poison" in effect:
        return "poison"

    if "shockwave" in effect:
        return "stun"

    if "shock" in effect:
        return "shock"

    if "stun" in effect:
        return "stun"

    if "protection" in effect or "aura" in effect:
        return "defence"

    if "rage" in effect:
        return "stun"

    if "melee damage" in effect:
        return "melee"

    if "soul" in effect:
        return "soul"

    if "damage" in effect:
        return "damage"

    return "balanced"


def recommend_relic(relics, boss_weights):
    results = []

    for relic in relics:
        effect = relic.get("Effect", "")
        profile_name = get_relic_profile(effect)

        profile = RELIC_PROFILES.get(profile_name, {
            stat: 1 / 6 for stat in [
                "Strength", "Defence", "Runic",
                "Vitality", "Cooldown", "Luck"
            ]
        })

        score = sum(
            float(boss_weights.get(stat, 0)) * affinity
            for stat, affinity in profile.items()
        )

        result = relic.copy()
        result["Profile"] = profile_name
        result["Score"] = round(score, 4)

        results.append(result)

    return sorted(
        results,
        key=lambda item: item["Score"],
        reverse=True
    )